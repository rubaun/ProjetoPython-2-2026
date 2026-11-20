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

# ================= (ESTATÍSTICAS) =================

    def resumo_estatistico(self):
        """Exibe estatísticas gerais de lucro e tempo de crescimento."""
        if self.df.empty:
            return
        print("\n--- RESUMO DA FAZENDA (STARDEW VALLEY) ---")
        media_lucro = (self.df['sell_price'] - self.df['seed_price']).mean()
        maior_venda = self.df['sell_price'].max()
        cultura_top = self.df.loc[self.df['sell_price'].idxmax(), 'crop_name']
        print(f"Média de lucro (Venda - Custo) por semente: {media_lucro:.2f} ouros")
        print(f"Cultura com maior preço de venda: {cultura_top} ({maior_venda:.0f} ouros)")

    def analise_por_estacao(self):
        """Agrupa os dados por estação do ano usando groupby()."""
        if self.df.empty:
            return
        print("\n--- MÉDIA DE PREÇO DE VENDA POR ESTAÇÃO ---")
        agrupado = self.df.groupby('season')['sell_price'].mean().sort_values(ascending=False)
        for estacao, media in agrupado.items():
            print(f"{estacao}: {media:.2f} ouros em média")

    def filtrar_por_estacao(self, estacao):
        """Filtra as sementes de uma estação específica."""
        if self.df.empty:
            return
        filtrado = self.df[self.df['season'].str.upper() == estacao.upper()]
        if filtrado.empty:
            print(f"Nenhuma cultura encontrada para a estação '{estacao}'.")
        else:
            print(f"\n--- TOP CULTURAS DA ESTAÇÃO: {estacao.upper()} ---")
            top5 = filtrado.sort_values(by='sell_price', ascending=False).head(5)
            for _, row in top5.iterrows():
                print(f"- {row['crop_name']}: Compra {row['seed_price']}G | Vende {row['sell_price']}G (Cresce em {row['days_to_grow']} dias)")


