import requests
import json
import base64
import urllib.parse


def send_get_json(url):
    with open('../config.json', 'r') as f:
        config = json.load(f)
    proxy = config['proxy']
    if proxy == "":
        return requests.get(url).json()
    else:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        return requests.get(url, proxies=proxies).json()


def get_base64(text):
    return base64.b64encode(text.encode()).decode()


def get_base64_url(text):
    return urllib.parse.quote(base64.b64encode(text.encode()).decode())