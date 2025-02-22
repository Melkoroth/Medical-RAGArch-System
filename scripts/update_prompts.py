
import requests
import os

# Función para rotar automáticamente el Token de GitHub usando OIDC
def rotate_github_token():
    oidc_token = os.getenv('ACTIONS_ID_TOKEN_REQUEST_TOKEN')
    oidc_url = os.getenv('ACTIONS_ID_TOKEN_REQUEST_URL')
    response = requests.get(oidc_url, headers={'Authorization': f'Bearer {oidc_token}'})
    if response.status_code == 200:
        return response.json().get('value')
    else:
        raise Exception('Error al obtener el Token de GitHub mediante OIDC.')

# Función para sincronizar prompts desde GitHub usando el Token rotado
def sync_prompts_from_github():
    token = rotate_github_token()
    headers = {"Authorization": f"token {token}"}
    response = requests.get("https://api.github.com/repos/Melkoroth/Medical-RAGArch-Prompts/contents/prompts.json", headers=headers)
    if response.status_code == 200:
        with open('./data/prompts/prompts.json', 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f'Error al sincronizar prompts: {response.status_code}')

if __name__ == "__main__":
    sync_prompts_from_github()
