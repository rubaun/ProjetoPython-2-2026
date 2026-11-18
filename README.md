📝 Projeto Final – Sistema de Análise de Vendas

👥 Integrantes da Equipe

[Natanael Silva de Souza] - [2025.15.1371]
[Ulisses dos Santos Martins] - [2026.15.98]
[João Victor Bernardino Silva] - [2026.15.296]
[Daniel de Oliveira Dias] - [2026.15.375]

🗂️ Sobre o Dataset Escolhido

Tema Geral: Análise de Vendas de Produtos e Categorias.

Fonte de Dados (URL):
https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

Motivação:

Escolhemos essa base de dados para analisar informações sobre vendas, produtos, categorias e anos de comercialização. Nosso objetivo é identificar quais categorias apresentam maior volume de vendas e visualizar o comportamento das vendas ao longo dos anos, utilizando estatísticas e gráficos.

🏗️ Arquitetura e Estruturação (O que vocês codaram)

Módulos / Classes Criadas:

Foi criada a classe AnalisadorVendas, localizada no arquivo src/analisador.py. Essa classe é responsável por carregar, limpar e processar os dados, realizar cálculos estatísticos, agrupar as vendas por categoria e gerar os gráficos para visualização das informações.

O arquivo main.py contém o menu interativo, permitindo que o usuário escolha as análises que deseja realizar.

Limpeza de Dados:

Foi utilizada a biblioteca Pandas para realizar a leitura do arquivo CSV. No construtor da classe, foi aplicado o método dropna() para remover registros com valores nulos. Também foram realizadas conversões de colunas numéricas e remoção de registros inválidos, garantindo maior qualidade dos dados utilizados nas análises.

📊 Gráficos Desenvolvidos

Visão 1: Gráfico de Linhas – Vendas por Ano

Apresenta a evolução do total de vendas ao longo dos anos. Foi utilizado o agrupamento groupby() pela coluna YEAR_ID, permitindo comparar os valores de vendas entre os diferentes anos.

Visão 2: Gráfico de Barras – Vendas por Categoria

Apresenta o total de vendas de cada categoria de produtos, permitindo identificar quais categorias tiveram maior participação nas vendas. As categorias são apresentadas em português para facilitar a compreensão.

Visão 3: Histograma – Distribuição dos Valores de Vendas

Apresenta a distribuição dos valores de vendas, permitindo observar a frequência com que diferentes faixas de valores aparecem na base de dados. Foi utilizado um filtro booleano para considerar apenas vendas positivas.
