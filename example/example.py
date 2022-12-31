import fofa


def userinfo():
    return handle.userinfo()


def search(query_text):
    return handle.search(query_text)


handle = fofa.Client()


# print(userinfo()) # 获取user info

# field =  ['ip','port','title','icp']
# print(handle.search('domain="qq.com"',field=field,size=10)) # 演示4.查询10个域名有关“qq.com”的资产，并且获取其IP、端口、标题和ICP备案号

