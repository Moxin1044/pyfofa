# FOFA SDK使用说明文档

### FOFA API

[`FOFA API`](https://fofa.info/api) 是资产搜索引擎 [`FOFA `](https://fofa.info/) 为开发者提供的 RESTful API接口, 允许开发者在自己的项目中集成 FOFA 的功能。

------

### FOFA SDK

基于 FOFA API编写的 python 版 SDK, 方便 python 开发者快速将 FOFA集成到自己的项目中

# 调用方法

### 配置文件

------

配置文件位于根目录下的`config.json`

```json
{
    "email":"***",
    "key":"***",
    "api_url":"https://fofa.info/api/v1",
    "proxy":""
}
```

proxy默认为空，如需代理，可对其进行填写。

|  `Email`  | 用户登陆 `FOFA ` 使用的`Email`                               |
| :-------: | :----------------------------------------------------------- |
|   `Key`   | 前往 [**`个人中心`**](https://fofa.info/userInfo) 查看 `API Key` |
| `api_url` | 没有事情请不要修改哦，这里是FOFA的API请求地址                |
|  `proxy`  | 用户定义的代理，格式为`127.0.0.1:8080`，如无需代理，请设置为空 |

#### 检查Fofa配置

------

```python
clients = Client()
print(clients.check_fofa_config())
```

只需要按照上述方法配置，即可检查配置信息。会在控制台输出你当前的`email`、`key`和`proxy`。

当然，每次执行前都会自动执行一次get_userinfo()，会根据您在config.json中填写的email和key进行获取信息。

# 调用示例

## 读取用户信息

### 代码示例

```python
import fofa


def userinfo(handle):
    print(handle.userinfo())

handle = fofa.Client()
userinfo(handle)
```

### 返回信息

```json
{
  "error": false,
  "email": "****@qq.com",
  "username": "***",
  "fcoin": 48,
  "isvip": true,
  "vip_level": 2,
  "is_verified": false,
  "avatar": "https://i.nosec.org/avatar/system/****",
  "message": "",
  "fofacli_ver": "4.0.3",
  "fofa_server": true
}
```

## 查询接口

### 代码示例

```Python
import fofa


def search(handle,query_text):
    return handle.search(query_text)

handle = fofa.Client()
print(search(handle,'title="bing"'))
```

### 返回信息

```json
{
  "error": false,
  "size": 8683,
  "page": 1,
  "mode": "extended",
  "query": "title\u003d\"bing\"",
  "results": [
    [
      "46.101.204.107",
      "hotel-bing.hotels-rimini-it.com",
      "80"
    ],
    [
      "104.21.32.129",
      "https://peapix.com",
      "443"
    ],
    [
      "193.8.37.83",
      "https://www.thorsmindecamping.dk",
      "443"
    ]
  ]
}
```

**注意：这里因为返回结果过多，所以修改了一下**

### 说明

`handle.search(query_text)`中，可以指定的传参如下：

```python
handle.search(query_text, field, page, size, full)
```

|   参数名   | 是否可空 |          默认值          | 传参类型 | 解释                                                         |
| :--------: | :------: | :----------------------: | :------: | ------------------------------------------------------------ |
| query_text |    否    |            无            |  string  | 需要进行查询的语句,即输入的查询内容                          |
|   field    |    是    | `['ip', 'host', 'port']` |   list   | 可选字段，默认host,ip,port，详见[附录1](https://fofa.info/api)或文末附录 |
|    page    |    是    |            1             |   int    | 是否翻页，默认为第一页，按照更新时间排序                     |
|    size    |    是    |           100            |   int    | 每页查询数量，默认为100条，最大支持10,000条/页               |
|    full    |    是    |          False           | boolean  | 默认搜索一年内的数据，指定为true即可搜索全部数据             |



------



## 获取

------

### 依赖

------

#### 库

```bash
pip install requests
```

------

### 环境

------

#### 开发环境

```
Win11 + Python3.10 + PyCharm 2022.2.3 (Professional Edition)
```

#### 使用环境

支持`python2.7+` 、`Python 3.x`环境

# 附录

## 查询接口（FOFA附录1）

| 序号 |     字段名      |                      描述                       |   权限   |
| :--: | :-------------: | :---------------------------------------------: | :------: |
|  1   |       ip        |                     ip地址                      |    无    |
|  2   |      port       |                      端口                       |    无    |
|  3   |    protocol     |                     协议名                      |    无    |
|  4   |     country     |                    国家代码                     |    无    |
|  5   |  country_name   |                     国家名                      |    无    |
|  6   |     region      |                      区域                       |    无    |
|  7   |      city       |                      城市                       |    无    |
|  8   |    longitude    |                  地理位置 经度                  |    无    |
|  9   |    latitude     |                  地理位置 纬度                  |    无    |
|  10  |    as_number    |                     asn编号                     |    无    |
|  11  | as_organization |                     asn组织                     |    无    |
|  12  |      host       |                     主机名                      |    无    |
|  13  |     domain      |                      域名                       |    无    |
|  14  |       os        |                    操作系统                     |    无    |
|  15  |     server      |                   网站server                    |    无    |
|  16  |       icp       |                    icp备案号                    |    无    |
|  17  |      title      |                    网站标题                     |    无    |
|  18  |      jarm       |                    jarm 指纹                    |    无    |
|  19  |     header      |                   网站header                    |    无    |
|  20  |     banner      |                   协议 banner                   |    无    |
|  21  |      cert       |                      证书                       |    无    |
|  22  |      body       |                  网站正文内容                   | 企业会员 |
|  23  |       fid       |                       fid                       | 企业会员 |
|  24  |   structinfo    | 结构化信息 (部分协议支持、比如elastic、mongodb) | 企业会员 |



## 聚合接口统计



### 统计聚合



### Host聚合

