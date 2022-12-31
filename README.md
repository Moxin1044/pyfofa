# FOFA SDK使用说明文档

### FOFA API

[`FOFA API`](https://fofa.info/api) 是资产搜索引擎 [`FOFA `](https://fofa.info/) 为开发者提供的 RESTful API接口, 允许开发者在自己的项目中集成 FOFA 的功能。

------

### FOFA SDK

基于 FOFA API编写的 python 版 SDK, 方便 python 开发者快速将 FOFA集成到自己的项目中。

更好的Markdown兼容阅读：https://m0x1n.easyctf.cn/moxin/13876

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
import pyfofa


handle = pyfofa.Client()
print(handle.check_fofa_config())
```

只需要按照上述方法配置，即可检查配置信息。会在控制台输出你当前的`email`、`key`和`proxy`。

当然，每次执行前都会自动执行一次get_userinfo()，会根据您在config.json中填写的email和key进行获取信息。

# 调用示例

---

## 读取用户信息

### 代码示例

```python
import pyfofa


handle = pyfofa.Client()
print(handle.userinfo())
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

---

## 查询接口

提供搜索主机、获取详细信息的方法，使开发更容易。

### 代码示例

```Python
import pyfofa


handle = pyfofa.Client()
print(handle.search('title="bing"'))
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

**注意：这里的field参数需要使用list传参哦**，query_text无需再base64编码。

#### 演示1.查询域名“qq.com”

```python
handle.search('domain="qq.com"')
```

#### 演示2.查询域名“qq.com”的第二页

```python
handle.search('domain="qq.com"',page=2)
```

#### 演示3.查询10个域名有关“qq.com”的资产

```python
handle.search('domain="qq.com"',size=10)
```

#### 演示4.查询10个域名有关“qq.com”的资产，并且获取其IP、端口、标题和ICP备案号

```python
field =  ['ip','port','title','icp']
handle.search('domain="qq.com"',field=field,size=10)
```

**注意：handle为`handle = fofa.Client()`，在环境中请不要忘了加上他哦！**

------

## 统计聚合

根据当前的查询内容，生成全球统计信息，当前可统计每个字段的前5排名。该接口限制请求并发为 5秒/次。

### 代码示例

```Python
import pyfofa


handle = pyfofa.Client()
print(handle.search_stats('ip="103.35.168.38"'))
```

### 返回信息

```json
{
  "error": false,
  "distinct": {
    "ip": 1,
    "title": 1
  },
  "aggs": {
    "countries": [],
    "title": [
      {
        "count": 1,
        "name": "RouterOS router configuration page"
      }
    ]
  },
  "lastupdatetime": "2022-06-11 07:00:00"
}
```

|  字段名  |                           描述                            |
| :------: | :-------------------------------------------------------: |
| distinct | 唯一计数 支持字段: ip, server, icp, domain,title,host,fid |
|   aggs   |                         聚合信息                          |

### 说明

`handle.search_stats(query_text)`中，可以指定的传参如下：

```python
handle.search(query_text, field)
```

|   参数名   | 是否可空 |          默认值          | 传参类型 | 解释                                                         |
| :--------: | :------: | :----------------------: | :------: | ------------------------------------------------------------ |
| query_text |    否    |            无            |  string  | 需要进行查询的语句,即输入的查询内容                          |
|   field    |    是    | `['ip', 'host', 'port']` |   list   | 可选字段，默认title，详见[附录2](https://fofa.info/api/stats/statistical)或文末附录 |

## Host聚合

根据当前的查询内容，生成聚合信息，host通常是ip，包含基础信息和IP标签。该接口限制请求并发为 1s/次。

### 代码示例

```python
import pyfofa


handle = pyfofa.Client()
print(handle.search_host('78.48.50.249'))
```

### 返回信息

```json
{
  "error": false,
  "host": "78.48.50.249",
  "ip": "78.48.50.249",
  "asn": 6805,
  "org": "Telefonica Germany",
  "country_name": "Germany",
  "country_code": "DE",
  "protocol": [
    "http",
    "sip",
    "https"
  ],
  "port": [
    8089,
    5060,
    7170,
    80,
    443
  ],
  "category": [
    "CMS"
  ],
  "product": [
    "Synology-WebStation"
  ],
  "update_time": "2022-12-29 05:00:00"
}
```

当detail=false时，默认为普通模式，返回结果如下：

|  字段名  |   描述   |
| :------: | :------: |
|   port   | 端口列表 |
| protocol | 协议列表 |
|  domain  | 域名列表 |
| categor  | 分类标签 |
| product  | 产品标签 |

当detail=true时，默认为详情模式，返回结果如下：

|     字段名     |                             描述                             |
| :------------: | :----------------------------------------------------------: |
|    products    |                         产品详情列表                         |
|    product     |                            产品名                            |
|    category    |                           产品分类                           |
|      leve      | l产品分层： 5 应用层， 4 支持层， 3 服务层，2 系统层， 1 硬件层， 0 无组件分层 |
| soft_hard_code |         产品是否为硬件；值为 1 是硬件，否则为非硬件          |



### 说明

`handle.search_stats(query_text)`中，可以指定的传参如下：

```python
handle.search_host(host, detail=False)
```

| 参数名 | 是否可空 | 默认值 | 传参类型 | 解释             |
| :----: | :------: | :----: | :------: | ---------------- |
|  host  |    否    |   无   |  string  | host名，通常是ip |
| detail |    是    | false  | boolean  | 显示端口详情     |

## 获取用户名

### 代码示例

```python
import pyfofa

handle = pyfofa.Client()
print(handle.username)
```

### 返回信息

```
Moxin
```

**(具体会返回用户名)**

## 获取F币数量

### 代码示例

```python
import pyfofa

handle = pyfofa.Client()
print(handle.fcoin)
```

### 返回信息

```
48
```

**（这里是整数型哦）**

## 获取VIP状态

### 代码示例

```python
import pyfofa

handle = pyfofa.Client()
print(handle.isvip)
```

### 返回信息

```
true
```

**（这里是布尔型）**

## 获取VIP等级

### 代码示例

```python
import pyfofa

handle = pyfofa.Client()
print(handle.viplevel)
```

### 返回信息

```
2
```

**（这里是整数型哦）**

## 获取头像链接

### 代码示例

```python
import pyfofa

handle = pyfofa.Client()
print(handle.avatar)
```

### 返回信息

```http
https://i.nosec.org/avatar/system/users/avatars/100/083/883/medium/3774a8c7500fc0a110aa957a1a3040c2_1.jpg?1671089293
```

**（这里是String哦）**

> **声明：通过上述方法进行`获取用户名`、`获取F币数量`、`获取VIP状态`、`获取VIP等级`、`获取头像链接`均不需要再次请求，变量是在初始化Client中默认进行并存储的，所以不会再次产生资源消耗。**

# 使用

### 依赖

------

#### 需要安装的库

```bash
pip install requests
```

#### 一般不需要安装的库

```
json、base64、urllib
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



## 聚合接口统计（FOFA附录2）

| 序号 |     字段名      |      描述       | 权限 |
| :--: | :-------------: | :-------------: | :--: |
|  1   |    protocol     |      协议       |  无  |
|  2   |     domain      |      域名       |  无  |
|  3   |      port       |      端口       |  无  |
|  4   |      title      |    http 标题    |  无  |
|  5   |       os        |    操作系统     |  无  |
|  6   |     server      | http server信息 |  无  |
|  7   |     country     | 国家、城市统计  |  无  |
|  8   |    as_number    |     asn编号     |  无  |
|  9   | as_organization |     asn组织     |  无  |
|  10  |   asset_type    |    资产类型     |  无  |
|  11  |       fid       |    fid 统计     |  无  |
|  12  |       icp       |   icp备案信息   |  无  |

# pythonfofa

pythonfofa是在PyPi中的一个库，与本仓库类似，但是只是定义email、key和proxy的方式不同。

仓库地址为：https://github.com/Moxin1044/pythonfofa

PyPi地址：https://pypi.org/project/pythonfofa/1.0.0/

