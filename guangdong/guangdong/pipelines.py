# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem 
from scrapy.conf import settings
import time
import pymssql
import pandas as pd

class GaungdongPipeline(object):
    def process_item(self, item, spider):
        return item

class MsSQLDALPipeline(object):

	def __init__(self):
		self.conn = ""
    #pipeline默认调用
	def process_item(self, item, spider):
		#获取数据库列表集合
		conn = self.conn
		sql="select or_name from mes_guangdongss"
		df = pd.read_sql(sql,conn)
		df=df.dropna()
		df.columns = ['or_name']
		or_name_set=set(df['or_name'])
		#插入信息		
		cursor = self.conn.cursor()
		or_name=item['or_name']
		#修改插入语句及setting文件
		insert_cont={"mes_gd":(item['credit_num'],item['re_num'],item['or_name'],item['or_type'],item['or_date'],item['manager'],item['person']
			,item['address'],item['city'])}
		#对应表格插入数据
		if or_name not in or_name_set:
			data = cursor.execute(settings['QUERY']["mes_gd"],insert_cont['mes_gd'])
			self.conn.commit()
			return data
		else:
			raise DropItem()

	def open_spider(self, spider):
		host = settings['MSSQL_SERVER']
		user = settings['MSSQL_USER']
		password = settings['MSSQL_PASSWORD']
		database = settings['MSSQL_DB']
		self.conn = pymssql.connect(host,user,password,database,charset="utf8")
	def close_spider(self, spider):
		self.conn.close()