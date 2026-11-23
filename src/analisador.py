import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDados:
    def __init__(self, caminho_csv):
        if not os.path.exists(caminho_csv):
            raise FileNotFoundError(f"Arquivo não encontrado no caminho: {caminho_csv}")

        # 1. Leitura do CSV
        df_bruto = pd.read_csv(caminho_csv)
        total_inicial = len(df_bruto)

        # 2. Rotina de limpeza técnica (remoção de nulos e duplicados)
        self.df = df_bruto.dropna().drop_duplicates().copy()

        # Garante tipagem numérica correta após limpeza
        colunas_numericas = ["temporada", "gols_pro", "gols_contra", "chutes", "posse_bola"]
        for col in colunas_numericas:
            self.df[col] = pd.to_numeric(self.df[col], errors="coerce")

        self.df = self.df.dropna()
        self.df["temporada"] = self.df["temporada"].astype(int)
        self.df["gols_pro"] = self.df["gols_pro"].astype(int)
        self.df["gols_contra"] = self.df["gols_contra"].astype(int)

        removidos = total_inicial - len(self.df)
        print(f"✅ Base carregada com sucesso! ({len(self.df)} registros válidos | {removidos} nulos/duplicados removidos)")

    def obter_resumo_estatistico(self):
        """Calcula médias e estatísticas gerais da base limpa."""
        media_gols = self.df["gols_pro"].mean()
        media_chutes = self.df["chutes"].mean()
        media_posse = self.df["posse_bola"].mean()
        max_gols = self.df["gols_pro"].max()

        print("\n📊 === ESTATÍSTICAS GERAIS DA BASE ===")
        print(f"• Total de partidas analisadas : {len(self.df)}")
        print(f"• Média de gols marcados       : {media_gols:.2f} por jogo")
        print(f"• Média de chutes a gol        : {media_chutes:.2f} por jogo")
        print(f"• Média de posse de bola       : {media_posse:.1f}%")
        print(f"• Recorde de gols em 1 jogo    : {max_gols} gols")

    def agrupar_por_time(self):
        """Agrupa os dados por equipe usando .groupby()."""
        agrupado = (
            self.df.groupby("time")
            .agg(
                partidas=("gols_pro", "count"),
                total_gols=("gols_pro", "sum"),
                media_gols=("gols_pro", "mean"),
                media_posse=("posse_bola", "mean"),
            )
            .sort_values(by="total_gols", ascending=False)
        )

        print("\n🏆 === DESEMPENHO AGRUPADO POR TIME ===")
        print(agrupado.round(2).to_string())

    def filtrar_por_time(self, nome_time):
        """Filtra partidas de um time específico (case-insensitive)."""
        filtro = self.df[self.df["time"].str.lower() == nome_time.strip().lower()]

        if filtro.empty:
            times_disponiveis = ", ".join(sorted(self.df["time"].unique()))
            print(f"\n⚠️ Nenhum registro encontrado para '{nome_time}'.")
            print(f"Times disponíveis na base: {times_disponiveis}")
            return

        print(f"\n🔍 === PARTIDAS FILTRADAS: {filtro['time'].iloc[0].upper()} ===")
        print(filtro[["temporada", "time", "adversario", "gols_pro", "gols_contra", "chutes", "posse_bola"]].to_string(index=False))

    def grafico_barras_gols_por_time(self):
        """Gráfico 1 (Barras): Total de gols marcados por equipe."""
        dados = (
            self.df.groupby("time")["gols_pro"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        plt.figure(figsize=(10, 5))
        sns.barplot(data=dados, x="time", y="gols_pro", hue="time", palette="viridis", legend=False)
        plt.title("Total de Gols Marcados por Equipe")
        plt.xlabel("Equipe")
        plt.ylabel("Total de Gols")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    def grafico_linha_evolucao_temporada(self):
        """Gráfico 2 (Linha): Média de gols por temporada."""
        dados = (
            self.df.groupby("temporada")["gols_pro"]
            .mean()
            .reset_index()
        )

        plt.figure(figsize=(9, 5))
        sns.lineplot(data=dados, x="temporada", y="gols_pro", marker="o", linewidth=2.5, color="#e63946")
        plt.title("Evolução da Média de Gols por Temporada")
        plt.xlabel("Temporada (Ano)")
        plt.ylabel("Média de Gols por Partida")
        plt.xticks(dados["temporada"])
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

    def grafico_dispersao_chutes_vs_gols(self):
        """Gráfico 3 (Dispersão): Relação entre finalizações (chutes) e gols marcados."""
        plt.figure(figsize=(9, 5))
        sns.scatterplot(
            data=self.df,
            x="chutes",
            y="gols_pro",
            hue="time",
            s=110,
            palette="deep"
        )
        plt.title("Relação entre Chutes a Gol e Gols Marcados")
        plt.xlabel("Quantidade de Chutes na Partida")
        plt.ylabel("Gols Marcados")
        plt.legend(title="Equipe", bbox_to_anchor=(1.02, 1), loc="upper left")
        plt.grid(True, linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()