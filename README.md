
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

* Pedro Quartieri
* Braynt Eduardo
* Gabriel Cavalheiro
* Kauan Souza

### 🗂️ Sobre o Dataset Escolhido

* **Tema Geral:** Vendas globais da indústria de videogames.
* **Fonte de Dados (URL):** https://www.kaggle.com/datasets/gregorut/videogamesales
* **Motivação:** A base reúne dados históricos de vendas de jogos físicos em diferentes regiões (América do Norte, Europa, Japão e demais mercados), plataformas e gêneros. O objetivo da análise foi identificar a evolução do mercado ao longo dos anos e descobrir quais gêneros concentram o maior volume de vendas globais.

### 🏗️ Arquitetura e Estruturação (O que vocês codaram)

* **Módulos / Classes Criadas:** Em `src/analisador.py` foram implementadas a classe abstrata `AnalisadorBase` (definindo o contrato com `@abstractmethod`) e a subclasse `AnalisadorDeDados`, responsável por carregar o CSV com `Pandas`, encapsular o DataFrame no atributo privado `self.__df`, aplicar filtros booleanos, agrupamentos com `.groupby()` e gerar os gráficos com `Matplotlib` e `Seaborn`. O arquivo `main.py` gerencia apenas o menu interativo CLI em laço `while True` com tratamento de exceções (`ValueError`).
* **Limpeza de Dados:** A base original possui 16.598 registros, apresentando valores nulos nas colunas `Year` e `Publisher` (307 linhas incompletas no total). A limpeza foi encapsulada no método privado `__limpar_dados()`, executado automaticamente no construtor da classe por meio de `.dropna(inplace=True)` e conversão da coluna `Year` para inteiro, resultando em 16.291 registros válidos.

### 📊 Gráficos Desenvolvidos

Descreva detalhadamente as 3 visualizações construídas:

1. **Visão 1:** Gráfico de linha (`sns.lineplot`) exibindo a evolução das vendas globais (em milhões de unidades) agrupadas por ano de lançamento com `.groupby("Year")["Global_Sales"].sum()`.
2. **Visão 2:** Gráfico de barras (`sns.barplot`) ordenando o total de vendas globais por gênero de jogo em ordem decrescente, permitindo comparar rapidamente os segmentos mais rentáveis.
3. **Visão 3:** Histograma com curva de densidade KDE (`sns.histplot`) filtrando jogos lançados a partir de 1995 (`Year >= 1995`) para visualizar a distribuição da quantidade de lançamentos ao longo das décadas.
