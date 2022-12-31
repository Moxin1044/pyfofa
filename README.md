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
    "email":"xxx@qq.com",
    "key":"fofa_key",
    "proxy":""
}
```

proxy默认为空，如需代理，可对其进行填写。

| `Email` | 用户登陆 `FOFA ` 使用的 `Email`                              |
| ------- | ------------------------------------------------------------ |
| `Key`   | 前往 [**`个人中心`**](https://fofa.info/userInfo) 查看 `API Key` |

#### 检查Fofa配置

------

```python
clients = Client()
print(clients.check_fofa_config())
```

只需要按照上述方法配置，即可检查配置信息。会在控制台输出你当前的`email`、`key`和`proxy`。

当然，每次执行前都会自动执行一次get_userinfo()，会根据您在config.json中填写的email和key进行获取信息。

## 示例

```

```

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

## 查询接口



## 聚合接口统计



### 统计聚合



### Host聚合

