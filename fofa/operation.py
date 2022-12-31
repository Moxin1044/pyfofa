import requests
import base64


def send_get_json(url):
    response = requests.get(url).json()
    return response


def get_base64(text):
    return base64.b64encode(text.encode()).decode()