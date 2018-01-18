from scrapy.spiders import Spider
from guangdong.items import GuangdongItem
from scrapy import Request
from bs4 import BeautifulSoup
#from guangdong.creat_table import Table
import re
from scrapy.conf import settings
import pypinyin

class Guangdongspider(Spider):
	name = 'mes_guangdongss'
	# dict_url=get_url(self)
	# start_urls = list(dict_url.keys())
	# keyword=re.compile(r"row\d+")
	#返回dict_url,参考jupyer:format及map函数
	def get_url():
		#抓取的城市
		list1=settings['URLS']
		#url形式
		url='http://{}.npo.gdnpo.gov.cn/home/publist2/webmjzzlist'
		#得到首字母
		list2=list(map(lambda x: pypinyin.slug(x, style=pypinyin.FIRST_LETTER,separator=''),list1))
		#得到具体的url
		list3=list(map(lambda x:url.format(x),list2))
		dict_url=dict(zip(list3,list1))
		return dict_url
	dict_url=get_url()
	start_urls = list(dict_url.keys())
	keyword=re.compile(r"row\d+")
	def parse(self,response):
		keyword=Guangdongspider.keyword
		dict_url=Guangdongspider.dict_url
		item = GuangdongItem()
		res = response.body
		soup = BeautifulSoup(res,'html.parser')
		data = soup.find_all('tr',class_=keyword)
		#去掉后缀
		origin_url=response.url[:response.url.find('mjzzlist')+8]
		for or_item in data:
			or_detail=or_item.find_all('td')
			item['credit_num']=or_detail[0].get_text().strip()
			item['re_num']=or_detail[1].get_text().strip()
			item['or_name']=or_detail[2].get_text().strip()
			item['or_type']=or_detail[3].get_text().strip()
			item['or_date']=or_detail[4].get_text().strip()
			item['manager']=or_detail[5].get_text().strip()
			item['person']=or_detail[6].get_text().strip()
			item['address']=or_detail[-1].get_text().strip()
			item['city']=dict_url[origin_url]
			yield item
		next_url = soup.find('div',class_='next').find('a')['href']
		#下一页链接
		or_next_url=origin_url+next_url[next_url.find('?'):]
		if next_url:
			yield Request(or_next_url)

