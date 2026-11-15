# Arquivo: analisador.py
# Aqui fica a classe que lê, limpa e analisa os dados do projeto.
# Base usada: Sleep Health and Lifestyle Dataset (Kaggle)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDeDados:

    def __init__(self, caminho_arquivo):
        # Lendo o arquivo CSV com o Pandas
        self.df = pd.read_csv(caminho_arquivo)
        self.total_inicial = len(self.df)

        # LIMPEZA DOS DADOS
        # Na coluna "Sleep Disorder", quem não tem distúrbio aparece como "None".
        # O Pandas entende "None" como vazio, então o dropna() apagaria essas pessoas.
        # Por isso trocamos o vazio por "Nenhum" antes de usar o dropna().
        self.df["Sleep Disorder"] = self.df["Sleep Disorder"].fillna("Nenhum")

        # Removendo linhas com dados vazios e linhas repetidas
        self.df = self.df.dropna()
        self.df = self.df.drop_duplicates()

        # Traduzindo os distúrbios para português
        self.df["Sleep Disorder"] = self.df["Sleep Disorder"].replace("Insomnia", "Insônia")
        self.df["Sleep Disorder"] = self.df["Sleep Disorder"].replace("Sleep Apnea", "Apneia do sono")

        self.total_final = len(self.df)

        # Deixando os gráficos com visual limpo
        sns.set_theme(style="whitegrid")

        # Mostrando todas as colunas das tabelas no terminal
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", 200)

    def mostrar_resumo(self):
        print("Registros no arquivo original:", self.total_inicial)
        print("Registros depois da limpeza:", self.total_final)
        print("Linhas removidas:", self.total_inicial - self.total_final)
        print()
        print("Primeiras linhas da base:")
        colunas = ["Gender", "Age", "Occupation", "Sleep Duration", "Quality of Sleep", "Sleep Disorder"]
        print(self.df[colunas].head())

    def mostrar_estatisticas(self):
        print("Idade média:", round(self.df["Age"].mean(), 1), "anos")
        print("Média de horas de sono:", round(self.df["Sleep Duration"].mean(), 2), "horas")
        print("Menor tempo de sono:", self.df["Sleep Duration"].min(), "horas")
        print("Maior tempo de sono:", self.df["Sleep Duration"].max(), "horas")
        print("Qualidade média do sono:", round(self.df["Quality of Sleep"].mean(), 2), "(de 1 a 10)")
        print("Nível médio de estresse:", round(self.df["Stress Level"].mean(), 2), "(de 1 a 10)")
        print("Média de passos por dia:", round(self.df["Daily Steps"].mean()))

    def media_sono_por_profissao(self):
        # Agrupando por profissão e calculando a média de horas de sono
        media = self.df.groupby("Occupation")["Sleep Duration"].mean()
        media = media.sort_values(ascending=False).round(2)
        print("Média de horas de sono por profissão:")
        print(media)

    def filtrar_por_disturbio(self, disturbio):
        # Filtrando só as pessoas que têm o distúrbio escolhido
        grupo = self.df[self.df["Sleep Disorder"] == disturbio]
        print("Grupo:", disturbio)
        print("Quantidade de pessoas:", len(grupo))
        print("Média de horas de sono:", round(grupo["Sleep Duration"].mean(), 2))
        print("Qualidade média do sono:", round(grupo["Quality of Sleep"].mean(), 2))
        print("Nível médio de estresse:", round(grupo["Stress Level"].mean(), 2))

    def filtrar_por_horas(self, horas):
        # Filtrando quem dorme pelo menos a quantidade de horas informada
        grupo = self.df[self.df["Sleep Duration"] >= horas]
        print(len(grupo), "pessoas dormem", horas, "horas ou mais.")
        if len(grupo) > 0:
            print("Qualidade média do sono desse grupo:", round(grupo["Quality of Sleep"].mean(), 2))

    def grafico_barras(self):
        # Gráfico de barras: qualidade média do sono por profissão
        media = self.df.groupby("Occupation")["Quality of Sleep"].mean().sort_values()
        plt.figure(figsize=(10, 6))
        plt.barh(media.index, media.values, color="steelblue")
        plt.title("Qualidade média do sono por profissão")
        plt.xlabel("Qualidade do sono (1 a 10)")
        plt.ylabel("Profissão")
        plt.tight_layout()
        plt.show()

    def grafico_linha(self):
        # Gráfico de linha: média de horas de sono por idade
        media = self.df.groupby("Age")["Sleep Duration"].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(media.index, media.values, marker="o", color="steelblue")
        plt.title("Média de horas de sono por idade")
        plt.xlabel("Idade (anos)")
        plt.ylabel("Horas de sono (média)")
        plt.tight_layout()
        plt.show()

    def grafico_histograma(self):
        # Histograma: como as horas de sono estão distribuídas
        plt.figure(figsize=(10, 6))
        plt.hist(self.df["Sleep Duration"], bins=10, color="steelblue", edgecolor="white")
        plt.title("Distribuição das horas de sono")
        plt.xlabel("Horas de sono por noite")
        plt.ylabel("Quantidade de pessoas")
        plt.tight_layout()
        plt.show()

    def grafico_dispersao(self):
        # Gráfico de dispersão: estresse x qualidade do sono
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x="Stress Level", y="Quality of Sleep", hue="Sleep Disorder")
        plt.legend(title="Distúrbio do sono")
        plt.title("Nível de estresse x Qualidade do sono")
        plt.xlabel("Nível de estresse (1 a 10)")
        plt.ylabel("Qualidade do sono (1 a 10)")
        plt.tight_layout()
        plt.show()
