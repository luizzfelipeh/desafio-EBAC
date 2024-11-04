# GitHub Trending Projects Scraper
Este projeto realiza uma extração automática dos 10 projetos mais populares do GitHub usando Python. Ele coleta informações sobre o ranking dos projetos, nome, linguagem de programação, quantidade de estrelas, estrelas do dia e forks, e salva esses dados em um arquivo CSV.

## Descrição do Projeto
O código faz scraping da página de projetos em alta do GitHub (https://github.com/trending) e extrai os seguintes dados:

* Ranking: posição do projeto entre os 10 mais populares
* Nome do Projeto: nome do repositório GitHub
* Linguagem de Programação: linguagem usada no projeto
* Estrelas: total de estrelas do repositório
* Estrelas do Dia: número de estrelas recebidas no dia
* Forks: total de forks do repositório

## Dependências
Para executar o código, você precisará das seguintes bibliotecas:

* requests: para realizar a solicitação HTTP
* BeautifulSoup (da biblioteca bs4): para analisar o HTML
* csv: para salvar os dados extraídos em um arquivo CSV

Instale as dependências com:

> bash
>
> pip install requests beautifulsoup4

## Como Usar
1. Clone o repositório e navegue até o diretório do projeto.
2. Execute o script Python:

> bash
> 
> python scraper.py
3. Após a execução, um arquivo top_projetos_github.csv será gerado no diretório, contendo as informações dos projetos.

## Tratamento de Erros
O código inclui um bloco try-except que lida com possíveis erros na solicitação HTTP, exibindo uma mensagem de erro se a página não puder ser carregada.
