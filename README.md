# Análise de Dados com Python

**Disciplina:** Linguagem de Programação em Python (2026.2)  
**Professor:** Ruben Prado  
**Instituição:** Faculdade de Tecnologia e Inovação Senac-DF  

---

## Objetivo do Projeto
Este projeto consolida os conhecimentos do semestre. As equipes atuam como Engenheiros de Dados para desenvolver um **Sistema Analítico Interativo (CLI)**. 

O sistema deve ler uma base de dados real (Kaggle), processá-la usando a biblioteca **Pandas**, estruturar a inteligência de negócios em **Orientação a Objetos (Classes)** e gerar *insights* visuais através do **Matplotlib/Seaborn**.

## Requisitos Técnicos Obrigatórios
1. **Menu Interativo (`main.py`):** Loop contínuo (`while`) com opções numéricas e tratamento de erros (`try/except`) para evitar travamentos.
2. **Motor de Dados:** Uso de Pandas para ler o arquivo `.csv`, tratar dados nulos (`dropna` ou `fillna`) e aplicar filtros ou agrupamentos (`groupby`).
3. **Orientação a Objetos:** A lógica de análise deve estar isolada em métodos dentro de uma ou mais Classes no diretório `src/`.
4. **Inteligência Visual:** O sistema deve ter opções que gerem, no mínimo, **3 gráficos diferentes** com eixos e títulos bem definidos.

---

## Como Entregar (Fluxo Git/GitHub)
Para simular o mercado de trabalho, a entrega não será um arquivo compactado, mas sim um **Pull Request (PR)**.

1. Faça o **Fork** (ou Clone, se usar o Classroom) deste repositório.
2. Crie uma branch de desenvolvimento para a sua equipe: `git checkout -b dev-nome-da-equipe`.
3. Não escrevam código diretamente na branch `main`.
4. Façam `commits` frequentes detalhando a construção do sistema.
5. Quando finalizado, subam a branch (`git push origin dev-nome-da-equipe`) e abram um **Pull Request** para a avaliação do professor.

---

## Instalação e Execução
Para testar o projeto na sua máquina local, instale as dependências:
```bash
# 1. Instalar bibliotecas
pip install -r requirements.txt

# 2. Executar o sistema
python main.py
