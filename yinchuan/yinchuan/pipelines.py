# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from http.client import SWITCHING_PROTOCOLS
from itemadapter import ItemAdapter
import json
from scrapy.exporters import JsonItemExporter
import pymysql
import datetime


'''def dbHandle():
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = '123456',
        db = 'jeecg-boot',
        charset = 'utf8',
        use_unicode = False
    )
    #conn.cursor().execute("truncate table `dwgk`")
    return conn'''

class YinchuanPipeline:

    
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = '123456',
            db = 'jeecg-boot',
            charset = 'utf8',
            use_unicode = False
        )
        self.cur = self.conn.cursor()
        
        #清空数据库的数据
        #self.cur.execute("truncate table articles" )

    def close_spider(self, spider):
        
        self.conn.commit()
        self.conn.close()
        print("Successful!")

    def insert_db(self, item):
        import datetime


        values = (
            item['column'],
            item['sub_column'],
            item['title'],
            item['href'],
            datetime.datetime.strptime(item['date'],'%Y-%m-%d')
            
        )   
        #print(name)
        sql = "INSERT INTO articles (lanmu, sub_lanmu, title, href, release_date) VALUES(%s, %s, %s,%s,%s)"
        self.cur.execute(sql, values)   
        
    def process_item(self, item, spider):
       
        self.insert_db(item)
        return item
    
    #def process_item(self, item, spider):
    #       return item
    
