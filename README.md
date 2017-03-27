# sbdspider
sobaidupan.com 的百度网盘爬虫

关于本工具介绍 [Python基于Scrapy框架写个麻雀虽小五脏俱全的爬虫](https://uublog.com/article/20170328/python-scrapy-ipproxy/)

## Installation

1. 导入MySQL数据
```
#mysql -u<username> -p 
> create database yzy_data;
> grant all on yzy_data.* to yzy_data@localhost identified by '<yourpassword>';
> flush privileges;
# mysql -u<username> -p yzy_data < yzy_data.sql

```
2. 安装[IPProxyPool](https://github.com/qiyeboy/IPProxyPool)
3. `git clone https://github.com/onecer/sbdspider.git`
4. `# nohup scrapy crawl sobaidu -s JOBDIR=crawls/sobaidu-1 1>/dev/null 2>logfile.log &`

## 工程目录

```
./
├── crawls # 开启持久化会产生一些记录文件
├── sbdspider
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── items.py     # 定义要采集的字段
│   ├── items.pyc
│   ├── middlewares  # 中间件 主要是随机选择 UserAgent和代理IP 主要用来反爬虫
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── RandomProxy.py
│   │   ├── RandomProxy.pyc
│   │   ├── RandomUserAgent.py
│   │   └── RandomUserAgent.pyc
│   ├── middlewares.py
│   ├── pipelines.py  # 入库MySQL
│   ├── pipelines.pyc
│   ├── scrapy_redis  # 用的九茶的模块 用Bloomfilter+redis去重
│   │   ├── BloomfilterOnRedis.py
│   │   ├── BloomfilterOnRedis.pyc
│   │   ├── connection.py
│   │   ├── connection.pyc
│   │   ├── dupefilter.py
│   │   ├── dupefilter.pyc
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── isExists.py
│   │   ├── pipelines.py
│   │   ├── queue.py
│   │   ├── queue.pyc
│   │   ├── scheduler.py
│   │   ├── scheduler.pyc
│   │   ├── spiders.py
│   │   ├── spiders.pyc
│   │   └── tests.py
│   ├── settings.py  # 配置 pipeline、middlewares的引用声明主要在这里
│   ├── settings.pyc
│   └── spiders
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── sobaidupan.py # 爬虫主体 主要是提取数据 分类
│       └── sobaidupan.pyc
└── scrapy.cfg

```

## 个人博客
- [weibo](http://weibo.com/yinyongyou)
- [uublog](https://uublog.com)
- [CSDN Blog](http://blog.csdn.net/MichaelJScofield)