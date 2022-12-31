import json
import requests
import base64


class Client:
    def __init__(self):
        self.username = None
        self.email_check = None
        # load config.json
        with open('../config.json', 'r') as f:
            config = json.load(f)
        self.email = config['email']
        self.key = config['key']
        self.proxy = config['proxy']
        self.get_userinfo()

    def check_fofa_config(self):
        return f"Email:{self.email} Key:{self.key} Proxy:{self.proxy}"

    def get_userinfo(self):
        # Check Email and key
        url = f"https://fofa.info/api/v1/info/my?email={self.email}&key={self.key}"
        response = requests.get(url).json()
        if response['error']:
            return response['errmsg']
        else:
            self.email_check = response['email']
            self.username = response['username']
            return self

    def search(self, query_text, field=None, page=1, size=100, full=False):
        if field is None:
            field = ['ip', 'host', 'port']
        fields = ','.join(field)
        query = base64.b64encode(query_text.encode())
        query = query.decode()
        url = f"https://fofa.info/api/v1/search/all?email={self.email}&key={self.key}&qbase64={query}&fields={fields}&page={page}&size={size}&full"


clients = Client()
clients.search("text")
