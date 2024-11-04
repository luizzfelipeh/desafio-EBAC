import requests
import pandas as pd
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import csv

URL = 'https://github.com/trending'

# Realizar a solicitação HTTP
try:
    resposta = requests.get(URL)
    resposta.raise_for_status()
    conteudo = resposta.text
except HTTPError as exc:
    print(exc)
    conteudo = None

# Prosseguir se a resposta foi bem-sucedida
if conteudo:
    soup = BeautifulSoup(resposta.content, 'html.parser')
    projetos = soup.find_all('article', class_='Box-row')[:10]

    # Lista para armazenar dados dos projetos
    top_projetos = []

    for ranking, projeto in enumerate(projetos, start=1):
        # Extrair nome do projeto
        nome_tag = projeto.find('span', class_='text-normal')
        nome = nome_tag.text.strip().replace('/', '') if nome_tag else "N/A"
        
        # Extrair linguagem
        language_tag = projeto.find('span', itemprop='programmingLanguage')
        language = language_tag.get_text().strip() if language_tag else "N/A"
        
        # Extrair estrelas totais
        stars_tag = projeto.find('a', class_='Link Link--muted d-inline-block mr-3')
        stars = stars_tag.get_text().strip() if stars_tag else "N/A"
        
        # Extrair estrelas de hoje
        stars_today_tag = projeto.find('span', class_='d-inline-block float-sm-right')
        stars_today = stars_today_tag.get_text().strip().split()[0] if stars_today_tag else "N/A"
        
        # Extrair forks
        forks_tag = projeto.find_all('a', class_='Link Link--muted d-inline-block mr-3')
        forks = forks_tag[1].get_text().strip() if len(forks_tag) > 1 else "N/A"

        # Adicionar dados do projeto à lista
        top_projetos.append([ranking, nome, language, stars, stars_today, forks])

    # Escrever dados no arquivo CSV
    with open('top_projetos_github.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['ranking', 'project', 'language', 'stars', 'stars_today', 'forks'])
        escritor_csv.writerows(top_projetos)

    print("Arquivo CSV 'top_projetos_github.csv' criado com sucesso!")

    top_projetos_df = pd.read_csv('top_projetos_github.csv')
    top_projetos_df