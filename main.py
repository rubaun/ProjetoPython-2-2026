
from src.analisador import AnalisadorDeDados

analisador = AnalisadorDeDados()

while True:
    print("\n===== ANÁLISE DE DESEMPENHO DOS ESTUDANTES =====")
    print("1 - Mostrar médias gerais")
    print("2 - Analisar preparação para o teste")
    print("3 - Analisar notas por gênero")
    print("4 - Gráfico de médias")
    print("5 - Histograma de matemática")
    print("6 - Gráfico de relação entre leitura e escrita")
    print("0 - Sair")

    try:
        opcao = int(input("\nEscolha uma opção: "))

    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        continue

    if opcao == 1:
        print("\nMédias gerais:")
        print(analisador.calcular_medias())

    elif opcao == 2:
        print("\nMédias por preparação:")
        print(analisador.analisar_preparacao())

    elif opcao == 3:
        genero = input("Digite female ou male: ").lower()

        if genero == "female" or genero == "male":
            print(analisador.analisar_genero(genero))
        else:
            print("Gênero inválido!")

    elif opcao == 4:
        analisador.grafico_medias()

    elif opcao == 5:
        analisador.grafico_distribuicao()

    elif opcao == 6:
        analisador.grafico_relacao()

    elif opcao == 0:
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("Opção inválida! Escolha uma opção do menu.")
