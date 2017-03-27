#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/13/17 12:48 PM
# @Author  : Onecer
# @Site    : uublog.com
# @File    : RandomProxy.py
# @Software: PyCharm Community Edition
# coding:utf-8
import random
from sbdspider import settings
import requests
import json

class RandomProxy(object):
    def __init__(self):  
        self.r = requests.get(u'http://127.0.0.1:8000/?types=0&count=&country=国内')
        self.ip_ports=json.loads(self.r.text)

    def process_request(self, request, spider):
        ip_port=random.choice(self.ip_ports)
        http_proxy="http://%s:%s"%(ip_port[0],ip_port[1])
        request.meta['proxy'] = http_proxy
