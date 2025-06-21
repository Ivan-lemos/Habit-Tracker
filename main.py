import requests
from datetime import datetime

# ---------------------------- CONSTANTES ------------------------------- #
# Substitua com suas próprias credenciais e IDs
USERNAME = "YOUR USERNAME"  # Seu nome de usuário Pixela
TOKEN = "YOUR SELF GENERATED TOKEN"  # Seu token de autenticação Pixela
GRAPH_ID = "YOUR GRAPH ID"  # O ID do gráfico que você deseja usar/criar

# Endpoint base da API Pixela
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# ---------------------------- FUNÇÕES DE INTERAÇÃO COM A API PIXELA ------------------------------- #

def create_user(username: str, token: str) -> requests.Response:
    """Cria um novo usuário na Pixela.

    Args:
        username (str): O nome de usuário desejado.
        token (str): O token de autenticação para o usuário.

    Returns:
        requests.Response: A resposta da requisição HTTP.
    """
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    return response


def create_graph(username: str, token: str, graph_id: str, graph_name: str, unit: str, graph_type: str, color: str) -> requests.Response:
    """Cria um novo gráfico para um usuário na Pixela.

    Args:
        username (str): O nome de usuário.
        token (str): O token de autenticação do usuário.
        graph_id (str): O ID único para o novo gráfico.
        graph_name (str): O nome de exibição do gráfico.
        unit (str): A unidade de medida para o gráfico (e.g., "Km", "cal").
        graph_type (str): O tipo de valor do gráfico (e.g., "int", "float").
        color (str): A cor do gráfico (e.g., "shibafu", "ajisai").

    Returns:
        requests.Response: A resposta da requisição HTTP.
    """
    graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    graph_config = {
        "id": graph_id,
        "name": graph_name,
        "unit": unit,
        "type": graph_type,
        "color": color
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    return response


def post_pixel(username: str, token: str, graph_id: str, date: str, quantity: str) -> requests.Response:
    """Registra um pixel (valor) em um gráfico específico para uma data.

    Args:
        username (str): O nome de usuário.
        token (str): O token de autenticação do usuário.
        graph_id (str): O ID do gráfico.
        date (str): A data no formato YYYYMMDD.
        quantity (str): O valor a ser registrado (como string).

    Returns:
        requests.Response: A resposta da requisição HTTP.
    """
    pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
    pixel_data = {
        "date": date,
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    return response


def update_pixel(username: str, token: str, graph_id: str, date: str, new_quantity: str) -> requests.Response:
    """Atualiza o valor de um pixel existente em um gráfico para uma data específica.

    Args:
        username (str): O nome de usuário.
        token (str): O token de autenticação do usuário.
        graph_id (str): O ID do gráfico.
        date (str): A data do pixel a ser atualizado no formato YYYYMMDD.
        new_quantity (str): O novo valor a ser registrado (como string).

    Returns:
        requests.Response: A resposta da requisição HTTP.
    """
    update_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"
    new_pixel_data = {
        "quantity": new_quantity
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    return response


def delete_pixel(username: str, token: str, graph_id: str, date: str) -> requests.Response:
    """Deleta um pixel (valor) de um gráfico para uma data específica.

    Args:
        username (str): O nome de usuário.
        token (str): O token de autenticação do usuário.
        graph_id (str): O ID do gráfico.
        date (str): A data do pixel a ser deletado no formato YYYYMMDD.

    Returns:
        requests.Response: A resposta da requisição HTTP.
    """
    delete_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.delete(url=delete_endpoint, headers=headers)
    return response

# ---------------------------- LÓGICA PRINCIPAL ------------------------------- #

if __name__ == "__main__":
    # Exemplo de uso:

    # 1. Criar um usuário (execute apenas uma vez)
    # print("Criando usuário...")
    # user_response = create_user(USERNAME, TOKEN)
    # print(user_response.text)

    # 2. Criar um gráfico (execute apenas uma vez após criar o usuário)
    # print("Criando gráfico...")
    # graph_response = create_graph(USERNAME, TOKEN, GRAPH_ID, "Cycling Graph", "Km", "float", "ajisai")
    # print(graph_response.text)

    # 3. Postar um pixel (registrar um valor para hoje)
    today = datetime.now()
    today_date_str = today.strftime("%Y%m%d")

    quantity_cycled = input("Quantos quilômetros você pedalou hoje? ")
    print("Postando pixel...")
    pixel_response = post_pixel(USERNAME, TOKEN, GRAPH_ID, today_date_str, quantity_cycled)
    print(pixel_response.text)

    # 4. Atualizar um pixel (exemplo: atualizar o valor de hoje)
    # print("Atualizando pixel...")
    # update_response = update_pixel(USERNAME, TOKEN, GRAPH_ID, today_date_str, "4.5")
    # print(update_response.text)

    # 5. Deletar um pixel (exemplo: deletar o valor de hoje)
    # print("Deletando pixel...")
    # delete_response = delete_pixel(USERNAME, TOKEN, GRAPH_ID, today_date_str)
    # print(delete_response.text)


