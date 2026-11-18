
from src.analisador import AnalisadorVendas


def menu():
    print("\n====================================")
    print("       SISTEMA DE ANALISE")
    print("             DE VENDAS")
    print("====================================")
    print("1 - Visualizar dados")
    print("2 - Estatisticas gerais")
    print("3 - Vendas por categoria")
    print("4 - Grafico de linhas")
    print("5 - Grafico de barras")
    print("6 - Histograma")
    print("0 - Sair")
    print("====================================")


def main():

    # Carregar o analisador e a base de dados
    try:
        analisador = AnalisadorVendas("data/vendas.csv")
        print("\nSistema iniciado com sucesso!")

    except FileNotFoundError:
        print("\nErro: arquivo vendas.csv nao encontrado!")
        print("Verifique se o arquivo esta dentro da pasta data.")
        return

    except Exception as erro:
        print(f"\nErro ao carregar os dados: {erro}")
        return

    # Menu interativo
    while True:

        menu()

        try:
            opcao = int(input("Escolha uma opcao: ").strip())

            if opcao == 1:
                analisador.visualizar_dados()

            elif opcao == 2:
                analisador.estatisticas_gerais()

            elif opcao == 3:
                analisador.vendas_por_categoria()

            elif opcao == 4:
                analisador.grafico_linhas()

            elif opcao == 5:
                analisador.grafico_barras()

            elif opcao == 6:
                analisador.grafico_histograma()

            elif opcao == 0:
                print("\nObrigado por utilizar o sistema!")
                print("Encerrando o programa...")
                break

            else:
                print("\nOpcao invalida!")
                print("Escolha uma opcao entre 0 e 6.")

        except ValueError:
            print("\nEntrada invalida!")
            print("Digite apenas numeros.")

        except Exception as erro:
            print(f"\nOcorreu um erro durante a operacao: {erro}")


if __name__ == "__main__":
    main()
