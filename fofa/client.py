import json
import requests

import operation

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
        response = operation.send_get_json(url)
        if response['error']:
            return response['errmsg']
        else:
            self.email_check = response['email']
            self.username = response['username']
            return self

    def userinfo(self):
        # Check Email and key
        url = f"https://fofa.info/api/v1/info/my?email={self.email}&key={self.key}"
        response = operation.send_get_json(url)
        if response['error']:
            return response['errmsg']
        else:
            return response

    def search(self, query_text, field=None, page=1, size=100, full=False):
        if field is None:
            field = ['ip', 'host', 'port']
        fields = ','.join(field)
        query = operation.get_base64(query_text)
        url = f"https://fofa.info/api/v1/search/all?email={self.email}&key={self.key}&qbase64={query}&fields={fields}&page={page}&size={size}&full={full}"
        response = operation.send_get_json(url)
        if response['error']:
            return response['errmsg']
        else:
            return response

    def search_stats(self,query_text, field=None, page=1, size=100):
        if field is None:
            field = ""
        fields = ','.join(field)
        query = operation.get_base64(query_text)
        print(query)


clients = Client()
print(clients.search("text"))
