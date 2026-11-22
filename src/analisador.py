import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDeDados:

    # Os 6 atributos de combate. São as colunas numéricas principais do projeto.
    COLUNAS_STATS = [
        "hp", "attack", "defense", "special_attack", "special_defense", "speed",
    ]

    # Colunas que PRECISAM existir no CSV para o sistema funcionar.
    COLUNAS_OBRIGATORIAS = [
        "pokedex_id", "name", "generation", "primary_type", "secondary_type",
        "base_stat_total", "is_legendary", "is_mythical", "is_baby",
    ] + COLUNAS_STATS

    # Colunas onde um valor vazio inviabiliza a análise (usadas no dropna).

    COLUNAS_ESSENCIAIS = ["name", "generation", "primary_type"] + COLUNAS_STATS

    # ------------------------------------------------------------------
    # CONSTRUTOR: leitura + limpeza
    # ------------------------------------------------------------------
    def __init__(self, caminho_csv: str) -> None:
        self.caminho_csv = caminho_csv

        # Leitura do arquivo (o separador deste CSV é a vírgula, o padrão).
        self.df = pd.read_csv(caminho_csv)

        self._validar_colunas()

        self.linhas_originais = len(self.df)
        self._limpar_dados()

        # Tema visual único para todos os gráficos.
        sns.set_theme(style="whitegrid")

    def _validar_colunas(self) -> None:
        """Garante que o CSV tem as colunas esperadas, com erro claro se faltar."""
        faltando = [c for c in self.COLUNAS_OBRIGATORIAS if c not in self.df.columns]
        if faltando:
            raise ValueError(
                "O CSV não tem as colunas esperadas: " + ", ".join(faltando)
            )

    def _limpar_dados(self) -> None:
        """Rotina de limpeza técnica dos dados (fillna + dropna + duplicados)."""

        # --- Passo 1: tratar o tipo secundário com fillna() -----------------
        self.nulos_tipo_secundario = int(self.df["secondary_type"].isna().sum())
        self.df["secondary_type"] = (
            self.df["secondary_type"].fillna("Nenhum").replace("None", "Nenhum")
        )

        # --- Passo 2: colunas verdadeiro/falso ------------------------------
        # Garante que is_legendary etc. sejam bool (vazio vira False).
        for coluna in ["is_legendary", "is_mythical", "is_baby"]:
            self.df[coluna] = self.df[coluna].fillna(False).astype(bool)

        # --- Passo 3: dropna() só nas colunas essenciais ---------------------
        antes = len(self.df)
        self.df = self.df.dropna(subset=self.COLUNAS_ESSENCIAIS)

        # --- Passo 4: remover duplicados -------------------------------------
        # pokedex_id é único por Pokémon; repetido significa linha duplicada.
        self.df = self.df.drop_duplicates(subset="pokedex_id")

        self.linhas_removidas = antes - len(self.df)

        # --- Passo 5: ajustar tipos e reorganizar o índice -------------------
        self.df = self.df.copy()
        self.df["generation"] = self.df["generation"].astype(int)
        self.df = self.df.reset_index(drop=True)

        if self.df.empty:
            raise ValueError("Nenhuma linha restou após a limpeza dos dados.")

    # ------------------------------------------------------------------
    # MÉTODO AUXILIAR (privado): usado por todos os gráficos
    # ------------------------------------------------------------------
    def _exibir(self) -> None:
        plt.tight_layout()
        plt.show()
        plt.close()

    # ------------------------------------------------------------------
    # OPÇÃO 1: visão geral (texto, sem gráfico)
    # ------------------------------------------------------------------
    def visao_geral(self) -> None:
        """Imprime um resumo do dataset e da limpeza aplicada."""
        print("\n" + "=" * 60)
        print("VISÃO GERAL DO DATASET")
        print("=" * 60)
        print(f"Arquivo: {self.caminho_csv}")
        print(f"Linhas originais: {self.linhas_originais}")
        print(f"Linhas removidas na limpeza: {self.linhas_removidas}")
        print(f"Pokémon analisados: {len(self.df)} | Colunas: {self.df.shape[1]}")
        print(
            f"Sem tipo secundário (tratado com fillna): "
            f"{self.nulos_tipo_secundario}"
        )

        # Média, mediana, mínimo e máximo de cada atributo de combate.
        print("\nResumo dos atributos de combate:")
        resumo = self.df[self.COLUNAS_STATS].agg(["mean", "median", "min", "max"])
        print(resumo.round(1).T.to_string())

        # groupby: poder total médio por geração (como o jogo evoluiu).
        media_geracao = self.df.groupby("generation")["base_stat_total"].mean()
        print("\nPoder total médio (base_stat_total) por geração:")
        for geracao, media in media_geracao.items():
            print(f"  Geração {geracao}: {media:.1f}")

        # Filtros booleanos: contagem das categorias especiais.
        total_lendarios = int(self.df["is_legendary"].sum())
        total_miticos = int(self.df["is_mythical"].sum())
        total_bebes = int(self.df["is_baby"].sum())
        print(
            f"\nLendários: {total_lendarios} | Míticos: {total_miticos} | "
            f"Bebês: {total_bebes}"
        )

        # idxmax: posição do maior valor; loc: pega a linha inteira dessa posição.
        mais_forte = self.df.loc[self.df["base_stat_total"].idxmax()]
        print(
            f"Maior poder total: {mais_forte['name']} "
            f"({int(mais_forte['base_stat_total'])})"
        )

    # ------------------------------------------------------------------
    # OPÇÃO 2: Pokémon por geração (barras)
    # ------------------------------------------------------------------
    def grafico_por_geracao(self) -> None:
        """Gráfico de barras: quantos Pokémon cada geração introduziu."""

        # groupby + size: conta as linhas de cada geração.
        contagem = self.df.groupby("generation").size()

        plt.figure(figsize=(9, 5))
        barras = plt.bar(
            contagem.index.astype(str), contagem.values, color="#3b6ea5"
        )
        plt.bar_label(barras, padding=3)  # escreve o valor em cima de cada barra
        plt.title("Quantidade de Pokémon por Geração")
        plt.xlabel("Geração")
        plt.ylabel("Quantidade de Pokémon")
        self._exibir()

    # ------------------------------------------------------------------
    # OPÇÃO 3: tipos primários (barras)
    # ------------------------------------------------------------------
    def grafico_tipos_primarios(self) -> None:
        """Gráfico de barras: quais tipos primários são mais comuns."""

        # groupby + size + sort_values: conta por tipo e ordena do maior p/ menor.
        contagem = (
            self.df.groupby("primary_type").size().sort_values(ascending=False)
        )

        plt.figure(figsize=(11, 6))
        sns.barplot(
            x=contagem.index.tolist(),
            y=contagem.values,
            hue=contagem.index.tolist(),  # hue = x só para aplicar a paleta
            palette="viridis",
            legend=False,
        )
        plt.xticks(rotation=45, ha="right")  # inclina os nomes para caber
        plt.title("Distribuição de Pokémon por Tipo Primário")
        plt.xlabel("Tipo primário")
        plt.ylabel("Quantidade de Pokémon")
        self._exibir()

    # ------------------------------------------------------------------
    # OPÇÕES 4 e 8: Top 10 (barras horizontais), via método auxiliar
    # ------------------------------------------------------------------
    def _grafico_top10(
        self, coluna: str, titulo: str, rotulo_x: str, cor: str
    ) -> None:
        """Monta um ranking dos 10 maiores valores de uma coluna."""

        # nlargest(10, coluna): as 10 linhas com maior valor naquela coluna.
        top10 = self.df.nlargest(10, coluna)

        plt.figure(figsize=(10, 6))
        barras = plt.barh(top10["name"].tolist(), top10[coluna].tolist(), color=cor)
        plt.gca().invert_yaxis()  # o maior fica no topo
        plt.bar_label(barras, padding=3)
        plt.title(titulo)
        plt.xlabel(rotulo_x)
        plt.ylabel("Pokémon")
        self._exibir()

    def grafico_top10_ataque(self) -> None:
        """Barras horizontais: os 10 Pokémon com maior ataque."""
        self._grafico_top10(
            "attack", "Top 10 Pokémon por Ataque", "Ataque (attack)", "#c0392b"
        )

    def grafico_top10_velocidade(self) -> None:
        """Barras horizontais: os 10 Pokémon mais rápidos."""
        self._grafico_top10(
            "speed", "Top 10 Pokémon Mais Rápidos", "Velocidade (speed)", "#f39c12"
        )

    # ------------------------------------------------------------------
    # OPÇÃO 5: dispersão ataque x defesa
    # ------------------------------------------------------------------
    def grafico_dispersao_ataque_defesa(self) -> None:
        """Dispersão: relação entre ataque e defesa, separando lendários."""

        # Coluna temporária só para o gráfico (não altera self.df).
        dados = self.df.assign(
            Grupo=self.df["is_legendary"].map(
                {True: "Lendário", False: "Não lendário"}
            )
        )
        # corr(): coeficiente de correlação (de -1 a 1) entre as duas colunas.
        correlacao = self.df["attack"].corr(self.df["defense"])

        plt.figure(figsize=(9, 6))
        sns.scatterplot(
            data=dados, x="attack", y="defense", hue="Grupo", alpha=0.7
        )
        plt.title(f"Ataque x Defesa (correlação = {correlacao:.2f})")
        plt.xlabel("Ataque (attack)")
        plt.ylabel("Defesa (defense)")
        self._exibir()

    # ------------------------------------------------------------------
    # OPÇÃO 6: histograma de HP
    # ------------------------------------------------------------------
    def grafico_histograma_hp(self) -> None:
        """Histograma: como os pontos de vida (HP) se distribuem."""
        media = self.df["hp"].mean()
        mediana = self.df["hp"].median()

        plt.figure(figsize=(9, 5))
        sns.histplot(data=self.df, x="hp", bins=20, kde=True, color="#27ae60")
        # Linhas verticais marcando média e mediana.
        plt.axvline(media, color="red", linestyle="--", label=f"Média: {media:.1f}")
        plt.axvline(
            mediana, color="black", linestyle=":", label=f"Mediana: {mediana:.1f}"
        )
        plt.legend()
        plt.title("Distribuição de HP dos Pokémon")
        plt.xlabel("HP (pontos de vida)")
        plt.ylabel("Quantidade de Pokémon")
        self._exibir()

    # ------------------------------------------------------------------
    # OPÇÃO 7: lendários vs não lendários (pizza)
    # ------------------------------------------------------------------
    def grafico_lendarios(self) -> None:

        # Filtros booleanos: ~ inverte True/False.
        lendarios = self.df[self.df["is_legendary"]]
        nao_lendarios = self.df[~self.df["is_legendary"]]

        print(
            f"\nPoder total médio -> Lendários: "
            f"{lendarios['base_stat_total'].mean():.1f} | "
            f"Não lendários: {nao_lendarios['base_stat_total'].mean():.1f}"
        )

        plt.figure(figsize=(7, 7))
        plt.pie(
            [len(lendarios), len(nao_lendarios)],
            labels=[
                f"Lendários ({len(lendarios)})",
                f"Não lendários ({len(nao_lendarios)})",
            ],
            autopct="%1.1f%%",
            startangle=90,
            explode=(0.08, 0),
            colors=["#8e44ad", "#95a5a6"],
        )
        plt.title("Pokémon Lendários vs Não Lendários")
        # A pizza não tem eixos, mas mantemos rótulos para seguir a regra do professor (título + xlabel + ylabel em todos os gráficos).
        plt.xlabel(f"Total analisado: {len(self.df)} Pokémon")
        plt.ylabel("Participação (%)")
        self._exibir()