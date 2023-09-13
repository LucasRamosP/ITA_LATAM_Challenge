import requests
import pandas as pd

URL = 'http://montreal.icea.decea.mil.br:5002/api/v1/'
TOKEN = 'a779d04f85c4bf6cfa586d30aaec57c44e9b7173'


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