# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class SbdspiderPipeline(object):
#    def process_item(self, item, spider):
#        return item

import json  
import MySQLdb
from scrapy.exceptions import DropItem
import settings

  
class SbdspiderPipeline(object):  
  
    def __init__(self):  
        self.file = open('items.jl', 'wb')  
  
    def process_item(self, item, spider):  
        line = json.dumps(dict(item)) + "\n"  
        self.file.write(line)  
        return item


# 入库到MySQL
class sobaiduPipeline(object):

    def __init__(self):
        self.conn=MySQLdb.connect(host=settings.MYSQL_HOST,
                                  user=settings.MYSQL_USER,
                                  passwd=settings.MYSQL_PASS,
                                  db=settings.MYSQL_NAME,
                                  charset='utf8',
                                  use_unicode=True)
        self.curosr = self.conn.cursor()

    def process_item(self,item,spider):
        try:
            userid = self.insert_user(item['uid'],item['name'],item['avatar'])
            sql="""INSERT INTO
                                yzy_resources(tid,cid,uid,title,size,url,pwd,description,available,sharetime)
                                VALUES('%d','%d','%d','%s','%s','%s','%s','%s','%d','%s')
                                """%(item['tid'],item['cid'],userid,item['title'],item['size'],item['url'],item['pwd'],item['description'],item['available'],item['sharetime'])
            vsql=sql.encode('utf8')
            self.curosr.execute(vsql)

        except MySQLdb.Error,e:
            print "Error:%d:%s" % (e.args[0],e.args[1])

        return item

    def insert_user(self,uid,name,pic):
        try:
            userid=0
            bSginal=self.curosr.execute("SELECT * FROM yzy_users WHERE uid='%s'"%(uid))
            if bSginal==1:
                results=self.curosr.fetchone()
                userid=results[0]
            else:
                sql = """INSERT INTO yzy_users(uid,uname,avatar)
                                    VALUES('%s','%s','%s')"""%(uid,name,pic)
                vsql = sql.encode('utf8')
                if self.curosr.execute(vsql)==1:
                    userid=self.curosr.lastrowid

        except MySQLdb.Error,e:
            print "Error:%d:%s" % (e.args[0], e.args[1])

        return userid