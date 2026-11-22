import sys
from src.analisador import AnalisadorDeDados

CAMINHO_CSV = "data/pokemon_gen1_to_gen9.csv"


def exibir_menu() -> None:
    """Exibe o menu principal formatado."""
    print("\n" + "=" * 60)
    print("   SISTEMA ANALÍTICO - POKÉDEX (GEN 1 a 9)")
    print("=" * 60)
    print("1 - Visão Geral do Dataset")
    print("2 - Pokémon por Geração           [Gráfico de Barras]")
    print("3 - Distribuição de Tipos Primários [Gráfico de Barras]")
    print("4 - Top 10 Pokémon por Ataque     [Barras Horizontais]")
    print("5 - Dispersão Ataque x Defesa     [Dispersão]")
    print("6 - Histograma de HP              [Histograma]")
    print("7 - Lendários vs Não-Lendários    [Gráfico de Pizza]")
    print("8 - Top 10 Pokémon Mais Rápidos   [Barras Horizontais]")
    print("0 - Sair")
    print("=" * 60)


def executar_opcao(analisador: AnalisadorDeDados, opcao: int) -> bool:
    """
    Executa a ação correspondente à opção escolhida.
    Retorna False quando o usuário deseja sair (opção 0).
    """
    if opcao == 0:
        print("\n Encerrando o sistema. Até logo!")
        return False

    acoes = {
        1: analisador.visao_geral,
        2: analisador.grafico_por_geracao,
        3: analisador.grafico_tipos_primarios,
        4: analisador.grafico_top10_ataque,
        5: analisador.grafico_dispersao_ataque_defesa,
        6: analisador.grafico_histograma_hp,
        7: analisador.grafico_lendarios,
        8: analisador.grafico_top10_velocidade,
    }

    acao = acoes.get(opcao)
    if acao is None:
        print("Opção inexistente. Digite um número do menu (0 a 8).")
        return True

    try:
        acao()
    except Exception as erro:
        # Protege o loop: erros dentro do método não quebram o sistema
        print(f"Falha ao executar a análise: {erro}")
    return True


def main() -> None:
    """Inicializa o analisador e executa o loop principal do menu."""
    print("\nCarregando o dataset da Pokédex...")

    try:
        analisador = AnalisadorDeDados(CAMINHO_CSV)
    except FileNotFoundError:
        print(f"ERRO: arquivo não encontrado em '{CAMINHO_CSV}'.")
        print("   Coloque o CSV em data/ e rode novamente.")
        sys.exit(1)
    except Exception as erro:
        print(f"ERRO ao carregar o CSV: {erro}")
        sys.exit(1)

    print("Dataset carregado com sucesso!")

    while True:
        exibir_menu()

        # ETAPA CRÍTICA: proteger a conversão com try/except (ValueError)
        try:
            entrada = input("\n Escolha uma opção: ").strip()
            opcao = int(entrada)
        except ValueError:
            print(" Entrada inválida! Digite apenas NÚMEROS inteiros.")
            continue
        except KeyboardInterrupt:
            print("\n\n Encerrando por interrupção do usuário.")
            break

        if not executar_opcao(analisador, opcao):
            break


if __name__ == "__main__":
    main()