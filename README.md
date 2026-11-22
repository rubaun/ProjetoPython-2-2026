
# Projeto: Análise de Dados com Python

**Disciplina:** Linguagem de Programação em Python (2026.2)  
**Professor:** Ruben Prado  
**Instituição:** Faculdade Senac-DF de Tecnologia e Inovação 

---

## Objetivo do Projeto
Este projeto consolida os conhecimentos do semestre. As equipes atuarão como Engenheiros de Dados para desenvolver um **Sistema Analítico Interativo (CLI - Command Line Interface)**. 

O sistema deve ler uma base de dados real (escolhida no Kaggle), processá-la usando a biblioteca **Pandas**, estruturar a inteligência de negócios através da **Orientação a Objetos (Classes)** e gerar *insights* visuais utilizando **Matplotlib/Seaborn**.

---

## Estrutura do Repositório (Como Organizar seu Código)
O projeto inicial que vocês clonaram já possui a arquitetura exigida para a entrega. **Não alterem essa estrutura básica**, apenas completem o código!

```text
projeto-integrador-python/
│
├── data/                   # Coloque aqui o arquivo .csv baixado do Kaggle.
│   └── .gitkeep            # Mantém a pasta visível no GitHub. Não apague.
│
├── src/                    # Pasta raiz do núcleo do sistema (Orientação a Objetos).
│   ├── __init__.py         # Indica ao Python que a pasta "src" é um módulo importável.
│   └── analisador.py       # Aqui vocês devem construir a Classe AnalisadorDeDados.
│                           # Toda a lógica de limpeza (Pandas) e gráficos fica aqui!
│
├── main.py                 # O Ponto de Entrada. É aqui que o laço 'while' do Menu Interativo roda.
├── requirements.txt        # Lista de bibliotecas externas obrigatórias do projeto.
├── .gitignore              # Configurado para não subir lixo de compilação (ex: __pycache__).
└── README.md               # Este arquivo. Vocês devem preencher o formulário no final!

```

---

## Requisitos Técnicos Obrigatórios (O que será avaliado)

1. **O Menu Interativo (`main.py`):**
O sistema deve rodar em um loop contínuo (`while True`). O menu numérico deve ser protegido com bloco `try/except` capturando `ValueError`. O programa não pode "dar tela de erro" se o usuário digitar uma letra.
2. **Motor de Dados (`analisador.py`):**
Uso exclusivo do Pandas para ler o `.csv`. A equipe deve aplicar pelo menos uma técnica de limpeza (`dropna()` ou `fillna()`) no construtor da classe. Antes de gerar um gráfico, a equipe deve utilizar comandos como `groupby` ou filtros booleanos.
3. **Arquitetura (Orientação a Objetos):**
A manipulação de dados e a geração de imagens **não podem** ser feitas soltas no `main.py`. A lógica de negócios deve ser inteiramente modelada como atributos e métodos (Ex: `self.df`) dentro da Classe no arquivo `analisador.py`.
4. **Inteligência Visual (Dashboards):**
O menu deve acionar métodos que gerem, no mínimo, **3 gráficos diferentes** (ex: Linha, Barras, Histograma, Dispersão). **Regra de Ouro:** Nenhum gráfico pode ser plotado sem título (`plt.title`) e nomes nos eixos (`plt.xlabel` e `plt.ylabel`).

---

## Como Entregar (Fluxo Git/GitHub)

Para simular o mercado de trabalho real de desenvolvimento de software, a entrega não será um arquivo compactado `.zip`, mas sim um **Pull Request (PR)** oficializado nesta plataforma.

1. Faça o **Fork** (ou Clone) deste repositório para a conta de um dos integrantes ou acesse o repositório gerado pela atividade.
2. É proibido programar diretamente na branch de produção. Crie a branch da equipe: `git checkout -b dev-nome-da-equipe`.
3. Escrevam o código nos arquivos disponibilizados fazendo `commits` frequentes. Dividam o trabalho!
4. Terminada a implementação, subam a branch para o servidor: `git push origin dev-nome-da-equipe`.
5. Abram um **Pull Request (PR)** apontando da branch de vocês para a `main`. O professor corrigirá e fará o merge deste PR.

---

## Instalação e Execução Local

Para testar o projeto no laboratório ou no computador de casa, abra o terminal e execute:

```bash
# 1. Instalar todas as dependências do projeto (Pandas, Matplotlib, Seaborn)
pip install -r requirements.txt

# 2. Iniciar o Menu Interativo
python main.py

```

---

# 📝 Formulário Oficial de Entrega (Preenchimento Obrigatório)

*(Atenção Equipe: Editem este arquivo README.md e preencham os campos abaixo antes de abrir o Pull Request).*

### 👥 Integrantes da Equipe

* Paulo Ruben Meira Prado 
* Vinícius Fernandes Dantas 
* Allana Matos 
* Gustavo Maciel dos Santos

### 🗂️ Sobre o Dataset Escolhido

* **Tema Geral:** Estatísticas de Pokémon (Gen 1 a 9)
* **Fonte de Dados (URL):** https://www.kaggle.com/datasets/abdurrahmanhakanacar/pokemon-gen-1-9-complete-stats-and-type-chart
* **Motivação:** O conjunto de dados reúne os atributos de combate (ataque, defesa, HP, velocidade), tipos e origens de todos os Pokémon das 9 gerações. A nossa curiosidade era analisar o balanceamento do jogo ao longo das gerações, identificando quais tipos dominam em força, como os status evoluíram e qual a diferença real de poder entre Pokémon comuns e lendários.


### 🏗️ Arquitetura e Estruturação (O que vocês codaram)

* **Módulos / Classes Criadas:** O projeto foi dividido em dois módulos com responsabilidades bem separadas, seguindo o princípio de separação de interesses (SoC):

main.py — camada de interface e controle. Não contém nenhuma lógica de dados: apenas exibe o menu, lê a entrada do usuário (com tratamento de ValueError e KeyboardInterrupt) e delega cada opção a um método público da classe analisadora. O dicionário acoes mapeia número → método, deixando o executar_opcao limpo e extensível. O bloco try/except em torno do AnalisadorDeDados(...) converte falhas de carregamento em mensagens amigáveis e encerra com sys.exit(1).

src/analisador.py — classe AnalisadorDeDados, o núcleo do sistema. Concentra toda a lógica:

Leitura do CSV via Pandas no construtor;
Validação de esquema (_validar_colunas) contra COLUNAS_OBRIGATORIAS;
Limpeza dos dados (_limpar_dados);
Cálculos analíticos com groupby, filtros booleanos, corr(), nlargest(), idxmax();
Geração dos gráficos com Matplotlib/Seaborn, com um método auxiliar privado _exibir() que padroniza layout, show() e close() — evitando vazamento de memória entre figuras.
A classe também centraliza constantes (COLUNAS_STATS, COLUNAS_OBRIGATORIAS, COLUNAS_ESSENCIAIS), garantindo que qualquer ajuste no esquema dos dados seja feito em um único ponto. O método privado _grafico_top10() reutiliza a lógica das opções 4 e 8, eliminando duplicação de código.

* **Limpeza de Dados:** A base tinha, sim, muitos valores nulos — mas não todos do mesmo tipo, e essa distinção foi o ponto-chave da limpeza:

secondary_type (nulos "informativos"): Pokémon de tipo único têm "None" no CSV, que o Pandas lê como NaN. Esses nulos representam quase metade do dataset e não são sujeira — são informação legítima ("não possui 2º tipo"). Por isso foi aplicado fillna("Nenhum") (com replace("None", "Nenhum") por segurança) em vez de dropna(). A quantidade tratada é registrada em self.nulos_tipo_secundario e reportada na visão geral.

Colunas booleanas (is_legendary, is_mythical, is_baby): preenchidas com fillna(False) e convertidas com .astype(bool), garantindo tipo consistente para os filtros booleanos (df[df["is_legendary"]] e df[~df["is_legendary"]]).

dropna() seletivo: aplicado apenas em COLUNAS_ESSENCIAIS (name, generation, primary_type + os 6 atributos de combate). Se falta nome, geração, tipo primário ou qualquer stat, o Pokémon é inútil para os gráficos e é removido. O secondary_type foi deliberadamente excluído dessa lista para não perder quase metade da base.

drop_duplicates(subset="pokedex_id"): como pokedex_id é único por Pokémon, linhas repetidas indicam duplicação real e são descartadas.

Pós-limpeza: generation é convertido para int, o índice é reorganizado com reset_index(drop=True), e uma checagem final (if self.df.empty) levanta ValueError caso a limpeza tenha esvaziado a tabela — falha explícita em vez de gráficos vazios silenciosos..

### 📊 Gráficos Desenvolvidos

Descreva detalhadamente as 3 visualizações construídas:

1. <img width="900" height="500" alt="Histograma de HP" src="https://github.com/user-attachments/assets/f4fe6c3a-27b4-4397-820d-f8de5683a78d" />

2. <img width="1104" height="485" alt="pokemon por geração" src="https://github.com/user-attachments/assets/6b49ad84-71aa-4f04-9ec0-97b0aa1583ae" />

3. <img width="1100" height="600" alt="Distribuição de tipos primarios" src="https://github.com/user-attachments/assets/611be1df-e2b3-4c29-970e-c99f8e8f6c8b" />


```
