import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDados:
    def __init__(self):
        """Construtor: carrega os 5 CSVs, junta tudo e aplica a limpeza técnica."""
        try:
            df_spring = pd.read_csv("data/spring_crops_info.csv")
            df_summer = pd.read_csv("data/summer_crops_info.csv")
            df_fall = pd.read_csv("data/fall_crops_info.csv")
            df_winter = pd.read_csv("data/winter_crops_info.csv")
            df_special = pd.read_csv("data/special_crops_info.csv")

            df_spring['season'] = 'Primavera'
            df_summer['season'] = 'Verão'
            df_fall['season'] = 'Outono'
            df_winter['season'] = 'Inverno'
            df_special['season'] = 'Especial'

            self.df = pd.concat(
                [df_spring, df_summer, df_fall, df_winter, df_special],
                ignore_index=True
            )
            self.df = self.df.dropna()
            self.df = self.df.drop_duplicates()

            print(f"Bases do Stardew Valley unidas com sucesso! Total de sementes: {len(self.df)}")
        except FileNotFoundError:
            print("Erro: Um ou mais arquivos CSV não foram encontrados na pasta 'data/'.")
            self.df = pd.DataFrame()
