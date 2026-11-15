# Arquivo: main.py
# Menu do nosso sistema. Aqui só tem o menu e as chamadas para a classe.
# Equipe:
#   Ana Júlia Sales Bernardes - 2026.15.55
#   Douglas Cerqueira da Silva - 2025.15.1407
#   Fabiane Rodrigues Sarres - 2026.15.129
#   Gustavo Augusto Rodrigues da Silva - 2026.15.71
#   Júlia da Silva Marques - 2026.15.242
#   Laryssa Cristine Andrade Almeida - 2025.15.1503
# ADS 2A - Faculdade SENAC-DF

from src.analisador import AnalisadorDeDados

try:
    analisador = AnalisadorDeDados("data/Sleep_health_and_lifestyle_dataset.csv")
except FileNotFoundError:
    print("Arquivo CSV não encontrado! Coloque o arquivo dentro da pasta data.")
    exit()

while True:
    print()
    print("===== ANALISADOR DE SONO E ESTILO DE VIDA =====")
    print("1 - Ver resumo da base")
    print("2 - Ver estatísticas gerais")
    print("3 - Média de sono por profissão")
    print("4 - Filtrar por distúrbio do sono")
    print("5 - Filtrar por horas de sono")
    print("6 - Gráfico de barras")
    print("7 - Gráfico de linha")
    print("8 - Histograma")
    print("9 - Gráfico de dispersão")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
        print()

        if opcao == 1:
            analisador.mostrar_resumo()
        elif opcao == 2:
            analisador.mostrar_estatisticas()
        elif opcao == 3:
            analisador.media_sono_por_profissao()
        elif opcao == 4:
            print("1 - Nenhum")
            print("2 - Insônia")
            print("3 - Apneia do sono")
            escolha = int(input("Escolha o distúrbio: "))
            if escolha == 1:
                analisador.filtrar_por_disturbio("Nenhum")
            elif escolha == 2:
                analisador.filtrar_por_disturbio("Insônia")
            elif escolha == 3:
                analisador.filtrar_por_disturbio("Apneia do sono")
            else:
                print("Opção inválida!")
        elif opcao == 5:
            horas = float(input("Digite a quantidade mínima de horas (ex: 7.5): "))
            analisador.filtrar_por_horas(horas)
        elif opcao == 6:
            analisador.grafico_barras()
        elif opcao == 7:
            analisador.grafico_linha()
        elif opcao == 8:
            analisador.grafico_histograma()
        elif opcao == 9:
            analisador.grafico_dispersao()
        elif opcao == 0:
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Digite um número do menu.")

    except ValueError:
        print("Entrada inválida! Digite apenas números.")
