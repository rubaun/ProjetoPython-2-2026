from src.analisador import AnalisadorDados


def exibir_menu():
    print("\n==========================================")
    print("   SISTEMA DE ANÁLISE - STARDEW VALLEY    ")
    print("==========================================")
    print("1. Ver resumo de lucro da fazenda")
    print("2. Ver média de venda por estação")
    print("3. Filtrar top culturas por estação (ex: Outono)")
    print("4. Gráfico: Média de Venda por Estação (Barras)")
    print("5. Gráfico: Custo vs Retorno (Dispersão)")
    print("6. Gráfico: Tempo de Crescimento (Histograma)")
    print("0. Sair")
    print("==========================================")


def main():
    analisador = AnalisadorDados()
    if analisador.df.empty:
        print("Encerrando o sistema...")
        return

    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n[ERRO] Entrada inválida! Por favor, digite apenas números.")
            continue

        if opcao == 1:
            analisador.resumo_estatistico()
        elif opcao == 2:
            analisador.analise_por_estacao()
        elif opcao == 3:
            estacao = input("Digite a estação (Primavera, Verão, Outono, Inverno, Especial): ")
            analisador.filtrar_por_estacao(estacao)
        elif opcao == 4:
            print("Gerando gráfico... (Feche a janela para continuar)")
            analisador.grafico_barras_estacoes()
        elif opcao == 5:
            print("Gerando gráfico... (Feche a janela para continuar)")
            analisador.grafico_dispersao_lucro()
        elif opcao == 6:
            print("Gerando gráfico... (Feche a janela para continuar)")
            analisador.grafico_histograma_crescimento()
        elif opcao == 0:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("\n[AVISO] Opção inexistente. Escolha um número entre 0 e 6.")


if __name__ == "__main__":
    main()
