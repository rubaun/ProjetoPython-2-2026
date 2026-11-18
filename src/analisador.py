
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorVendas:

    def __init__(self, caminho_arquivo):

        # Carregar arquivo CSV utilizando Pandas
        self.dados = pd.read_csv(
            caminho_arquivo,
            encoding="latin1"
        )

        # Verificar se as colunas necessarias existem
        colunas_obrigatorias = [
            "SALES",
            "YEAR_ID",
            "PRODUCTLINE"
        ]

        for coluna in colunas_obrigatorias:
            if coluna not in self.dados.columns:
                raise ValueError(
                    f"A coluna {coluna} nao foi encontrada no arquivo."
                )

        # Limpeza dos dados vazios
        self.dados.dropna(inplace=True)

        # Converter colunas para valores numericos
        self.dados["SALES"] = pd.to_numeric(
            self.dados["SALES"], errors="coerce"
        )

        self.dados["YEAR_ID"] = pd.to_numeric(
            self.dados["YEAR_ID"], errors="coerce"
        )

        # Remover registros invalidos
        self.dados.dropna(
            subset=["SALES", "YEAR_ID", "PRODUCTLINE"],
            inplace=True
        )

        # Remover vendas negativas ou iguais a zero
        self.dados = self.dados[
            self.dados["SALES"] > 0
        ]

        print("\nDados carregados e limpos com sucesso!")
        print("Total de registros:", len(self.dados))

    # Visualizar os dados
    def visualizar_dados(self):

        print("\n--- DADOS DA PLANILHA ---")
        print(self.dados.head(10).to_string(index=False))

    # Estatisticas gerais
    def estatisticas_gerais(self):

        print("\n--- ESTATISTICAS GERAIS ---")

        print(
            f"Total de vendas: R$ {self.dados['SALES'].sum():,.2f}"
        )

        print(
            f"Media das vendas: R$ {self.dados['SALES'].mean():,.2f}"
        )

        print(
            f"Maior venda: R$ {self.dados['SALES'].max():,.2f}"
        )

        print(
            f"Menor venda: R$ {self.dados['SALES'].min():,.2f}"
        )

        print(
            f"Quantidade de registros: {len(self.dados)}"
        )

    # Agrupamento de vendas por categoria
    def vendas_por_categoria(self):

        vendas = self.dados.groupby(
            "PRODUCTLINE"
        )["SALES"].sum().sort_values(ascending=False)

        # Traduzir categorias para portugues
        traducao = {
            "Classic Cars": "Carros Classicos",
            "Vintage Cars": "Carros Antigos",
            "Motorcycles": "Motocicletas",
            "Planes": "Avioes",
            "Ships": "Navios",
            "Trains": "Trens",
            "Trucks and Buses": "Caminhoes e Onibus"
        }

        vendas.index = vendas.index.map(
            lambda categoria: traducao.get(categoria, categoria)
        )

        print("\n--- VENDAS POR CATEGORIA ---")
        print(vendas.to_string())

    # Grafico de linhas
    def grafico_linhas(self):

        vendas = self.dados.groupby(
            "YEAR_ID"
        )["SALES"].sum().sort_index()

        plt.figure(figsize=(10, 5))

        plt.plot(
            vendas.index,
            vendas.values,
            marker="o",
            color="blue"
        )

        plt.title("Vendas por Ano")
        plt.xlabel("Ano")
        plt.ylabel("Total de Vendas (R$)")

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Grafico de barras
    def grafico_barras(self):

        vendas = self.dados.groupby(
            "PRODUCTLINE"
        )["SALES"].sum().sort_values(ascending=False)

        # Traduzir categorias para portugues
        traducao = {
            "Classic Cars": "Carros Classicos",
            "Vintage Cars": "Carros Antigos",
            "Motorcycles": "Motocicletas",
            "Planes": "Avioes",
            "Ships": "Navios",
            "Trains": "Trens",
            "Trucks and Buses": "Caminhoes e Onibus"
        }

        categorias = vendas.index.map(
            lambda categoria: traducao.get(categoria, categoria)
        )

        plt.figure(figsize=(10, 5))

        sns.barplot(
            x=categorias,
            y=vendas.values,
            color="steelblue"
        )

        plt.title("Vendas por Categoria de Produtos")
        plt.xlabel("Categoria de Produtos")
        plt.ylabel("Total de Vendas (R$)")

        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    # Histograma com filtro booleano
    def grafico_histograma(self):

        # Filtrar vendas positivas
        dados_filtrados = self.dados[
            self.dados["SALES"] > 0
        ]

        plt.figure(figsize=(10, 5))

        sns.histplot(
            data=dados_filtrados,
            x="SALES",
            bins=20,
            kde=True,
            color="green"
        )

        plt.title("Distribuicao dos Valores de Vendas")
        plt.xlabel("Valor das Vendas (R$)")
        plt.ylabel("Frequencia")

        plt.tight_layout()
        plt.show()