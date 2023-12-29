import requests
import json 

# Função para trazer os personagens
def trazer_personagens():
    url = "https://swapi.dev/api/people/"
    requisicao = requests.get(url)
    return requisicao.json()

# Função para trazer os planetas
def trazer_planetas():
    url = "https://swapi.dev/api/planets"
    requisicao = requests.get(url)
    return requisicao.json()

# Função para definir se o personagem participa de 4 filmes ou mais 
def personagens_em_4_filmes_ou_mais(persons):
    return [personagem for personagem in persons['results'] if len(personagem['films']) >= 4]

# Função para puxar planetas com 5 habitantes ou mais 
def planetas_com_5_moradores_ou_mais(planetas):
    return [planeta for planeta in planetas['results'] if len(planeta['residents']) >= 5]

# Função para criar um novo arquivo Json com as informações pedidas
def salvar_json(nome_arquivo, dados):   
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

if __name__ == "__main__":
    # Parte a) Consultar personagens em 4 filmes ou mais
    personagens = trazer_personagens()
    personagens_4_filmes_ou_mais = personagens_em_4_filmes_ou_mais(personagens)
    salvar_json("personagens_4_filmes_ou_mais.json", personagens_4_filmes_ou_mais)

    # Parte b) Consultar planetas com 5 moradores ou mais
    planetas = trazer_planetas()
    planetas_5_moradores_ou_mais = planetas_com_5_moradores_ou_mais(planetas)
    salvar_json("planetas_5_moradores_ou_mais.json", planetas_5_moradores_ou_mais)