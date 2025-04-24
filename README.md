# 📱 Sistema de Busca de Películas Compatíveis

Este projeto foi desenvolvido para facilitar o dia a dia de profissionais que trabalham com acessórios mobile. A aplicação permite pesquisar rapidamente quais películas 3D são compatíveis com diferentes modelos de smartphones, otimizando o atendimento e reduzindo erros na escolha da película correta.

## 🚀 Motivação

Trabalhando em loja de acessórios, notei que muitos modelos de celulares têm telas muito parecidas, o que torna difícil encontrar a película certa. Este sistema resolve esse problema com uma busca prática e eficiente, baseada em uma tabela personalizada.

## 🧠 Funcionalidades

- 🔍 Busca rápida por nome de modelo (ex: "note 12")
- 📋 Exibe lista de compatibilidades de forma organizada
- 💾 Leitura automática de planilha Excel
- 🌙 Interface em modo escuro com design limpo (CustomTkinter)

## 🛠️ Tecnologias Utilizadas

- Python 3
- [Pandas](https://pandas.pydata.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Planilhas Excel (.xlsx)

## 📂 Como Usar

1. Clone este repositório ou baixe o arquivo `.py`:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
2. Instale as dependências:
   ```bash
   pip install pandas openpyxl customtkinter
   ```
3. Coloque sua planilha com os dados (`tabela_peliculas_tabela_formatada.xlsx`) no mesmo diretório do script.
4. Execute o programa:
   ```bash
   python nome_do_arquivo.py
   ```

## 🧾 Estrutura Esperada da Planilha

A planilha deve conter ao menos duas colunas:
- `Modelo`: nome do aparelho
- `Compatíveis`: modelos com películas compatíveis

## ✍️ Autor

Desenvolvido por **Leonardo Andrade**, proprietário da OnTech – loja especializada em acessórios e soluções para dispositivos móveis.