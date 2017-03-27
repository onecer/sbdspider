# -*- coding: utf-8 -*-
from sbdspider.scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from sbdspider.items import SbdspiderItem
import requests
import re
import datetime

class SobaidupanSpider(RedisSpider):
    name = "sobaidu"
    # class type keymap
    ckm_music=('mp3','wav','mid','wma','cda','acc')
    # id 2
    ckm_picture=('jpg','jpeg','png','gif','psd','bmp','svg','tga')
    # id 3
    ckm_ebook=('txt','pdf','mobi','azw','mbp','ebx')
    # id 4
    ckm_docfile=('doc','docx','wps','ppt','xls','xlsx')
    # id 5
    ckm_app=('apk','ipa','sis','sisx','xap')
    # id 6
    ckm_torrent=('torrent')
    # id 7
    ckm_movie=('mkv','rmvb','mp4','rm','avi','wmv','asf','asx','mpg','mpeg','mpe','3gp','flv','f4v','vob','mov') 
    # id 8 
    ckm_apeflac=('ape','flac')
    # id 9
    ckm_teach=(u'教程',u'入门',u'精讲',u'详解',u'课程')
    # id 10
    allowed_domains = ["www.sobaidupan.com"]
    redis_key = "sobaidupan:start_urls"
    start_urls = ['http://www.sobaidupan.com/']
    
    def start_requests(self):
        for u in self.start_urls:
            yield Request(u,callback=self.parse,
                                    errback=self.errback)

    def parse(self, response):
        yield self.parse_item(response)
        for a in response.css('a::attr(href)').extract():
            if not a:
                continue
            next_url = response.urljoin(a)
            yield Request(next_url,callback=self.parse)
        
    def parse_item(self,response):
        uid = re.search('user-(\d*)-1\.html',response.text)
        name = re.search(u'<div align="center">用户名：(.+?)</div></td>',response.text)
        avatar = re.search('<img src="(.+?)" width="100" height="100" border="0">',response.text)
        title = re.search('<h1>(.+?)</h1>',response.text)
        ressize = re.search(u'<B>资源大小：</B>(.+?)&nbsp;<b>',response.text)
        description = re.search(u'<B>资源类别：</B>(.+?)</div>',response.text)
        sharetime = re.search(u'<b>分享日期：</b>(.+?)</div>',response.text)
        res = re.search('href="(http://sbdp\.baidudaquan\.com/down\.asp\?id=.+?)"',response.text)
        if res is not None and title is not None:
            ssource = requests.get(res.group(1))
            ssource.encoding = 'utf-8'
            resurl = re.search("URL=(.+?)'",ssource.text)
            # re.search("URL=(http://pan\.baidu\.com/share/link\?shareid=.+?)'",ssource.text)
            if resurl is not None:
                item = SbdspiderItem()
                item['tid'] = 1
                item['cid'] = self.classifyRes(title.group(1))
                item['uid'] = uid.group(1)
                item['name'] = name.group(1)
                item['avatar'] = avatar.group(1)
                item['title'] = title.group(1)
                if ressize is not None:
                    item['size'] = ressize.group(1)
                else:
                    item['size'] = '未知'
                item['url'] = resurl.group(1)
                item['pwd'] = ''
                if description is not None:
                    item['description'] = description.group(1)
                else:
                    item['description'] = ''
                item['available'] = 1
                if sharetime is not None:
                    item['sharetime'] = sharetime.group(1)
                else:
                    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    item['sharetime'] = dt
                return item
    
    # 大致给数据分类    
    def classifyRes(self,title):
        ext_title=''
        classid=1   # 初始化ID为1
        # 尝试提取后缀
        if len(title.split('.'))>=2:
            ext_title = title.split('.')[-1]
        else:
            ext_title = title
            ext_title.encoding = 'utf-8'
        
        # 按keymap分类
        if   ext_title in self.ckm_music:   
            classid = 2
        elif ext_title in self.ckm_picture:
            classid = 3
        elif ext_title in self.ckm_ebook:
            classid = 4
        elif ext_title in self.ckm_docfile:
            classid = 5
        elif ext_title in self.ckm_torrent:
            classid = 6
        elif ext_title in self.ckm_app:
            classid = 7
        elif ext_title in self.ckm_movie:
            classid = 8
        elif ext_title in self.ckm_apeflac:
            classid = 9
        else:
            for s in self.ckm_teach:
                if s in ext_title:
                    classid = 10
        return classid
            
    def errback(self, failure):
        pass
