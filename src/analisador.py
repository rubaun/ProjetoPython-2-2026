
import pandas as pd
import matplotlib.pyplot as plt


class AnalisadorDeDados:

    def __init__(self):
        self.dados = pd.read_csv("data/StudentsPerformance.csv")
        self.dados = self.dados.dropna()

    def calcular_medias(self):
        medias = self.dados[
            ["math score", "reading score", "writing score"]
        ].mean()

        return medias

    def analisar_preparacao(self):
        resultado = self.dados.groupby("test preparation course")[
            ["math score", "reading score", "writing score"]
        ].mean()

        return resultado

    def analisar_genero(self, genero):
        filtrados = self.dados[
            self.dados["gender"] == genero
        ]

        medias = filtrados[
            ["math score", "reading score", "writing score"]
        ].mean()

        return medias

    def grafico_medias(self):
        medias = self.calcular_medias()

        medias.plot(kind="bar")

        plt.title("Média das notas por matéria")
        plt.xlabel("Matérias")
        plt.ylabel("Média das notas")

        plt.show()

    def grafico_distribuicao(self):
        self.dados["math score"].plot(kind="hist", bins=10)

        plt.title("Distribuição das notas de matemática")
        plt.xlabel("Notas")
        plt.ylabel("Quantidade de estudantes")

        plt.show()

    def grafico_relacao(self):
        self.dados.plot(
            kind="scatter",
            x="reading score",
            y="writing score"
        )

        plt.title("Relação entre notas de leitura e escrita")
        plt.xlabel("Notas de leitura")
        plt.ylabel("Notas de escrita")

        plt.show()
