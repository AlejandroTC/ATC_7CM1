#ejemplo de SaaS
import requests
import json

def get_github_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)

    if response.status_ode == 200:
        data = response.json()
        print("Nombre del repositorio: {data('name')}")
        print("Descripcion: {data['description']}")
        print("Estrellas: {data['stargazers_count']}")
        print("Idioma principal: {data['language']}")
    else:
        print(f"No se pudo obtener informacion para el repositorio {owner}/{repo}, Estado HTTP: {response.status_code}")

#ejemplo de uso
#get_github_repo_info("Halex300486", "prueba01")
#get_github_repo_info("tensorflow", "tensorflow")
