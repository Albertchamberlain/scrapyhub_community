# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import pymysql
import pandas as pd

class XiaoquPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        # print(item['raw_title'])
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item


#选择2号数据库
r = redis.Redis(host='47.112.123.168', port=6379, db=2, password="houboxue", decode_responses=True)


from .settings import MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT

class XiaoquRedisPipeline(object):
    def __init__(self):
        host = MYSQL_HOST
        user = MYSQL_USER
        passwd = MYSQL_PASSWORD
        port = MYSQL_PORT
        db = MYSQL_DATABASE
        self.connection = pymysql.connect(host, user, passwd, db, port, charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        sql = "SELECT coord,detail_address FROM community_copy1 ";
        Xiaoqu_from_mysql = pd.read_sql(sql, self.connection)  # 从Mysql中读数据,返回DataFrame(数据帧)



        for i in range(0, Xiaoqu_from_mysql.shape[0]):     # 把每一小区具体地址写入
            #      print(Xiaoqu_from_mysql['detail_address'].iloc[i])
            #      print(Xiaoqu_from_mysql['coord'].iloc[i])
            #print("=======================================================================")
            r.set(Xiaoqu_from_mysql['coord'].iloc[i], Xiaoqu_from_mysql['detail_address'].iloc[i])
        return item


    def __del__(self, spider):
        self.connect.close()
