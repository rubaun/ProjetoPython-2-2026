
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

* [Nome do Integrante 1] - [Matrícula]
* [Nome do Integrante 2] - [Matrícula]
* [Nome do Integrante 3] - [Matrícula]

### 🗂️ Sobre o Dataset Escolhido

* **Tema Geral:** (Ex: Vendas de E-commerce, Estatísticas de E-sports, Saúde Pública, etc.)
* **Fonte de Dados (URL):** (Cole o link do Kaggle aqui)
* **Motivação:** (Explique em duas frases o que esses dados representam e qual problema ou curiosidade queriam analisar).

### 🏗️ Arquitetura e Estruturação (O que vocês codaram)

* **Módulos / Classes Criadas:** (Explique a responsabilidade da classe criada em `analisador.py`).
* **Limpeza de Dados:** (Descreva se a base tinha muitos dados nulos e qual técnica foi utilizada para limpá-la - ex: `.dropna()`).

### 📊 Gráficos Desenvolvidos

Descreva detalhadamente as 3 visualizações construídas:

1. **Visão 1:** (Ex: Gráfico de linha comparando a quantidade de chuva entre Jan e Fev).
2. **Visão 2:** (Ex: Gráfico de barras indicando os 5 produtos mais rentáveis da loja).
3. **Visão 3:** (Ex: Histograma validando a distribuição de idades na faixa de risco).

```
