# 数据库配置
DATABASE = {
    'default': {
        'DBTYPE': 'redis',
        'NAME': '0',
        'HOST': '127.0.0.1',
        'PORT': 6379,
        'USER': 'root',
        'PASSWORD': '',
        'HNAME': 'proxy'
    },
    'ssdb': {
        'DBTYPE': 'ssdb',
        'NAME': '0',
        'HOST': '127.0.0.1',
        'PORT': 6379,
        'USER': 'root',
        'PASSWORD': ''
    }
}
# flask 启动
SERVER_API = {
    'HOST': '127.0.0.1',
    'PORT': 5000,
    'DEBUG': True
}

# 代理IP爬虫
PROXY_GETTER = {
    "freeProxy01",
    "freeProxy02",
    "freeProxy03",
    "freeProxy04",
    "freeProxy05",
    "freeProxy06",
    "freeProxy07",
    "freeProxy08",
    "freeProxy09",
}

PROXY_DB_TABLES = {
    'raw': 'proxy',
    'useful': 'useful_proxy'
}