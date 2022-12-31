import json
import requests
import fofa.operation

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
        response = fofa.operation.send_get_json(url)
        if response['error']:
            return response['errmsg']
        else:
            self.email_check = response['email']
            self.username = response['username']
            return self

    def userinfo(self):
        # Check Email and key
        url = f"https://fofa.info/api/v1/info/my?email={self.email}&key={self.key}"
        response = fofa.operation.send_get_json(url)
        if response['error']:
            return response['errmsg']
        else:
            return response

    def search(self, query_text, field=None, page=1, size=100, full=False):
        if field is None:
            field = ['ip', 'host', 'port']
        fields = ','.join(field)
        query = fofa.operation.get_base64_url(query_text)
        url = f"https://fofa.info/api/v1/search/all?email={self.email}&key={self.key}&qbase64={query}&fields={fields}&page={page}&size={size}&full={full}"
        response = fofa.operation.send_get_json(url)
        '''
        # 考虑到生产环境，所以不可以在这里直接返回errmsg，统一返回response即可。
        # 下同
        if response['error']:
            return response['errmsg']
        else:
            return response
        '''
        return response

    def search_stats(self, query_text, field=None):
        if field is None:
            field = ['title']
        fields = ','.join(field)
        query = fofa.operation.get_base64_url(query_text)
        url = f"https://fofa.info/api/v1/search/stats?fields={fields}&qbase64={query}&email={self.email}&key={self.key}"
        response = fofa.operation.send_get_json(url)
        return response

    def search_host(self,host, detail=False):
        url = f"https://fofa.info/api/v1/host/{host}?detail={detail}&email={self.email}&key={self.key}"
        response = fofa.operation.send_get_json(url)
        return response


clients = Client()
print(clients.search_stats("text"))
