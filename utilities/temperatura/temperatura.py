import requests
from config import *

def clima(tipo, comando):
    api_key = venv_vars['api_owm_key']
    if tipo == "temperatura":

        cidade = comando

        # URL da API para buscar o clima por cidade
        url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&units=metric&q=" + cidade

        # Nome da cidade para buscar o clima
        

        # Faz a requisição à API para buscar o clima da cidade especificada
        response = requests.get(url)

        # Verifica se a requisição foi bem sucedida
        if response.status_code == 200:
            # Converte a resposta em formato JSON para um dicionário Python
            data = response.json()

            # Obtém a temperatura atual da cidade em graus Celsius
            temperatura = data['main']['temp']

            info = "A temperatura atual em " + cidade + " é de " + str(temperatura) + "°C."
            return info
        else:
            # Imprime uma mensagem de erro caso a requisição não tenha sido bem sucedida
            return 'Erro ao buscar clima.'
