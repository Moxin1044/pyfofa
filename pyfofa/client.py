import json
import requests
import pyfofa.operation


class Client:
    def __init__(self):
        self.username = None
        self.email_check = None
        # load config.json
        with open('../config.json', 'r') as f:
            config = json.load(f)
        self.email = config['email']
        self.key = config['key']
        self.url = config['api_url']
        self.get_userinfo()

    def check_fofa_config(self):
        return f"Email:{self.email} Key:{self.key} Proxy:{self.proxy}"

    def get_userinfo(self):
        # Check Email and key
        url = f"{self.url}/info/my?email={self.email}&key={self.key}"
        response = pyfofa.operation.send_get_json(url)
        if response['error']:
            return response['errmsg']
        else:
            self.email_check = response['email']
            self.username = response['username']
            self.isvip = response['isvip']
            self.viplevel = response['vip_level']
            self.avatar = response['avatar']
            self.fcoin = response['fcoin']
            return self

    def userinfo(self):
        # Check Email and key
        url = f"{self.url}/info/my?email={self.email_check}&key={self.key}"
        response = pyfofa.operation.send_get_json(url)
        if response['error']:
            return response['errmsg']
        else:
            return response

    def search(self, query_text, field=None, page=1, size=100, full=False):
        if field is None:
            field = ['ip', 'host', 'port']
        fields = ','.join(field)
        query = pyfofa.operation.get_base64_url(query_text)
        url = f"{self.url}/search/all?email={self.email_check}&key={self.key}&qbase64={query}&fields={fields}&page={page}&size={size}&full={full}"
        response = pyfofa.operation.send_get_json(url)
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
        query = pyfofa.operation.get_base64_url(query_text)
        url = f"{self.url}/search/stats?fields={fields}&qbase64={query}&email={self.email_check}&key={self.key}"
        response = pyfofa.operation.send_get_json(url)
        return response

    def search_host(self, host, detail=False):
        url = f"{self.url}/host/{host}?detail={detail}&email={self.email_check}&key={self.key}"
        response = pyfofa.operation.send_get_json(url)
        return response
