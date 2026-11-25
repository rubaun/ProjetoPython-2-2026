from pathlib import Path
from src.analisador import AnalisadorDeDados


def exibir_menu():
    print("\n" + "=" * 44)
    print("   SISTEMA ANALÍTICO DE DADOS - KAGGLE")
    print("=" * 44)
    print("1 - Resumo estatístico da base")
    print("2 - Filtrar vendas por gênero")
    print("3 - Gráfico de Linha: Vendas por ano")
    print("4 - Gráfico de Barras: Vendas por gênero")
    print("5 - Histograma: Lançamentos por ano")
    print("0 - Sair")
    print("=" * 44)


def iniciar_sistema():
    caminho = Path(__file__).resolve().parent / "data" / "vgsales.csv"
    meu_analisador = AnalisadorDeDados(caminho)

    if not meu_analisador.esta_pronto():
        return

    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite apenas o número da opção.")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrando o sistema.")
            break

        if opcao == 1:
            meu_analisador.resumo_estatistico()
        elif opcao == 2:
            genero = input("Digite o gênero (ex: Action, Sports, Role-Playing): ")
            meu_analisador.filtrar_por_genero(genero)
        elif opcao == 3:
            meu_analisador.grafico_linha_vendas_ano()
        elif opcao == 4:
            meu_analisador.grafico_barras_vendas_genero()
        elif opcao == 5:
            meu_analisador.grafico_histograma_anos()
        elif opcao == 0:
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inexistente! Escolha um número entre 0 e 5.")


if __name__ == "__main__":
    iniciar_sistema()
