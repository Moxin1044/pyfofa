import requests
import json
import base64


def send_get_json(url):
    with open('../config.json', 'r') as f:
        config = json.load(f)
    proxy = config['proxy']
    if not proxy:
        return requests.get(url).json()
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    return requests.get(url, proxies=proxies).json()



def get_base64(text):
    return base64.b64encode(text.encode()).decode()