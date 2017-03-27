#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/13/17 12:31 PM
# @Author  : Onecer
# @Site    : uublog.com
# @File    : RandomUseragent.py
# @Software: PyCharm Community Edition
# coding:utf-8
import random

class RandomUserAgent(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS')) 

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))