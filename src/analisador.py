from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorBase(ABC):
    """Classe abstrata que define o contrato mínimo para analisadores de dados."""

    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = Path(caminho_arquivo)

    @abstractmethod
    def resumo_estatistico(self):
        pass


class AnalisadorDeDados(AnalisadorBase):
    """Responsável por carregar, limpar, filtrar e visualizar os dados de vendas de games."""

    def __init__(self, caminho_arquivo):
        super().__init__(caminho_arquivo)
        self.__linhas_originais = 0
        self.__linhas_removidas = 0

        try:
            self.__df = pd.read_csv(self.caminho_arquivo)
            self.__linhas_originais = len(self.__df)
            self.__limpar_dados()
            print(
                f"Sistema Analítico iniciado. Dados limpos e prontos "
                f"({len(self.__df)} registros válidos; {self.__linhas_removidas} nulos removidos)."
            )
        except FileNotFoundError:
            print(
                f"Erro crítico: Arquivo '{self.caminho_arquivo}' não encontrado na pasta data/."
            )
            self.__df = None

    def __limpar_dados(self):
        """Método privado (encapsulado) para limpeza inicial da base."""
        if self.__df is not None:
            self.__df.dropna(inplace=True)
            self.__linhas_removidas = self.__linhas_originais - len(self.__df)
            if "Year" in self.__df.columns:
                self.__df["Year"] = self.__df["Year"].astype(int)

    def esta_pronto(self):
        return self.__df is not None

    def resumo_estatistico(self):
        """Exibe estatísticas descritivas gerais e os 5 jogos mais vendidos."""
        if self.__df is not None:
            print("\n--- RESUMO DA BASE DE DADOS ---")
            print(f"Registros originais: {self.__linhas_originais}")
            print(f"Registros removidos (nulos): {self.__linhas_removidas}")
            print(f"Total de registros válidos: {len(self.__df)}\n")
            print(self.__df.describe())

            top5 = self.__df.nlargest(5, "Global_Sales")[
                ["Name", "Platform", "Year", "Genre", "Global_Sales"]
            ]
            print("\n--- TOP 5 JOGOS MAIS VENDIDOS (EM MILHÕES) ---")
            print(top5.to_string(index=False))

    def filtrar_por_genero(self, genero):
        """Filtra a base por gênero e exibe total, média e top 3 jogos."""
        if self.__df is not None:
            filtro = self.__df["Genre"].str.lower() == genero.strip().lower()
            resultado = self.__df[filtro]

            if resultado.empty:
                generos = ", ".join(sorted(self.__df["Genre"].unique()))
                print(f"\nGênero '{genero}' não encontrado.")
                print(f"Gêneros disponíveis: {generos}")
                return

            media = resultado["Global_Sales"].mean()
            total = resultado["Global_Sales"].sum()
            top3 = resultado.nlargest(3, "Global_Sales")[
                ["Name", "Platform", "Year", "Global_Sales"]
            ]

            print(f"\n--- FILTRO: {genero.strip().upper()} ---")
            print(f"Jogos encontrados: {len(resultado)}")
            print(f"Vendas globais totais: {total:.2f} milhões")
            print(f"Média de vendas por jogo: {media:.2f} milhões")
            print("\nTop 3 jogos desse gênero:")
            print(top3.to_string(index=False))

    def grafico_linha_vendas_ano(self):
        """Visão 1: Gráfico de linha da evolução das vendas globais por ano."""
        if self.__df is not None:
            vendas_ano = self.__df.groupby("Year")["Global_Sales"].sum().reset_index()

            plt.figure(figsize=(10, 5))
            sns.lineplot(data=vendas_ano, x="Year", y="Global_Sales", marker="o")
            plt.title("Evolução das Vendas Globais de Games por Ano")
            plt.xlabel("Ano de Lançamento")
            plt.ylabel("Vendas Globais (em milhões)")
            plt.grid(True, linestyle="--", alpha=0.5)
            plt.tight_layout()
            plt.show()

    def grafico_barras_vendas_genero(self):
        """Visão 2: Gráfico de barras com o total de vendas globais por gênero."""
        if self.__df is not None:
            vendas_genero = (
                self.__df.groupby("Genre")["Global_Sales"]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
            )

            plt.figure(figsize=(10, 5))
            sns.barplot(data=vendas_genero, x="Genre", y="Global_Sales")
            plt.title("Total de Vendas Globais por Gênero")
            plt.xlabel("Gênero")
            plt.ylabel("Vendas Globais (em milhões)")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()

    def grafico_histograma_anos(self):
        """Visão 3: Histograma com curva KDE dos lançamentos a partir de 1995."""
        if self.__df is not None:
            jogos_recentes = self.__df[self.__df["Year"] >= 1995]

            plt.figure(figsize=(10, 5))
            sns.histplot(data=jogos_recentes, x="Year", bins=20, kde=True)
            plt.title("Distribuição de Lançamentos de Jogos (a partir de 1995)")
            plt.xlabel("Ano de Lançamento")
            plt.ylabel("Quantidade de Jogos")
            plt.tight_layout()
            plt.show()
