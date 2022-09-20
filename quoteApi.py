import requests
import json
def get_quote():
    url = 'https://zenquotes.io/api/random'
    res = requests.get(url)
    json_data = res.json()
    quote = f'''
       {json_data[0]['q']}

        --by  {json_data[0]['a'].upper()}
    '''
    return quote
