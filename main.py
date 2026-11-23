import os
from src.analisador import AnalisadorDados


def exibir_menu():
    print("\n" + "=" * 48)
    print("   ⚽ PAINEL DE ENGENHARIA DE DADOS - FUTEBOL   ")
    print("=" * 48)
    print("[1] Ver estatísticas gerais (Médias e Recordes)")
    print("[2] Ver ranking agrupado por time (.groupby)")
    print("[3] Filtrar partidas por time")
    print("[4] Gerar Gráfico de Barras (Gols por Time)")
    print("[5] Gerar Gráfico de Linha (Média por Temporada)")
    print("[6] Gerar Gráfico de Dispersão (Chutes vs Gols)")
    print("[0] Sair do sistema")
    print("=" * 48)


def main():
    caminho_csv = os.path.join("data", "dados_futebol.csv")

    try:
        analisador = AnalisadorDados(caminho_csv)
    except FileNotFoundError as erro:
        print(f"❌ Erro crítico: {erro}")
        return

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("❌ Entrada inválida! Digite apenas o número correspondente à opção.")
            continue

        if opcao == 1:
            analisador.obter_resumo_estatistico()
        elif opcao == 2:
            analisador.agrupar_por_time()
        elif opcao == 3:
            nome_time = input("Digite o nome do time (ex: Flamengo, Palmeiras): ")
            if not nome_time.strip():
                print("⚠️ O nome do time não pode ficar em branco.")
            else:
                analisador.filtrar_por_time(nome_time)
        elif opcao == 4:
            print("📈 Abrindo Gráfico de Barras... (feche a janela do gráfico para voltar ao menu)")
            analisador.grafico_barras_gols_por_time()
        elif opcao == 5:
            print("📈 Abrindo Gráfico de Linha... (feche a janela do gráfico para voltar ao menu)")
            analisador.grafico_linha_evolucao_temporada()
        elif opcao == 6:
            print("📈 Abrindo Gráfico de Dispersão... (feche a janela do gráfico para voltar ao menu)")
            analisador.grafico_dispersao_chutes_vs_gols()
        elif opcao == 0:
            print("👋 Encerrando o sistema de análise de dados. Até mais!")
            break
        else:
            print("❌ Opção inexistente! Escolha um número entre 0 e 6.")


if __name__ == "__main__":
    main()