import requests
import pandas as pd
from geopy.distance import great_circle

URL = 'http://montreal.icea.decea.mil.br:5002/api/v1/'
TOKEN = 'a779d04f85c4bf6cfa586d30aaec57c44e9b7173'

AEROPORTOS = {
    'SBBR': (-15.8698, -47.9208),  # Brasília
    'SBCF': (-19.6341, -43.9683),  # Confins
    'SBCT': (-25.5327, -49.1725),  # Curitiba
    'SBFL': (-27.6709, -48.5523),  # Florianópolis
    'SBGL': (-22.8076, -43.2504),  # Galeão
    'SBGR': (-23.4317, -46.4698),  # Guarulhos
    'SBKP': (-23.0074, -47.1345),  # Campinas
    'SBPA': (-29.9942, -51.1719),  # Porto Alegre
    'SBRF': (-8.1266, -34.9186),   # Recife
    'SBRJ': (-22.9107, -43.1631),  # Santos Dumont
    'SBSP': (-23.6277, -46.6564),  # Congonhas
    'SBSV': (-12.9136, -38.3312)   # Salvador
}


def request_api(endpoint:str, inicial_date, final_date):

    full_url = URL + endpoint

    body ={
        'token' : TOKEN,
        'idate': inicial_date,
        'fdate':final_date
    }
  
    response = requests.request(url = full_url, method='GET',params = body)
    
    response_data = response.json()
    df = pd.DataFrame(response_data)
    
    return df

def calcular_distancia(row):
    origem = row['origem']
    destino = row['destino']
    if origem in AEROPORTOS and destino in AEROPORTOS:
        coord_origem = AEROPORTOS[origem]
        coord_destino = AEROPORTOS[destino]
        distancia = great_circle(coord_origem, coord_destino).kilometers
        return distancia
    else:
        return None