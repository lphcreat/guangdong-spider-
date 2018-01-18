import requests
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy

engine = create_engine('mssql+pyodbc://cfc:!QAZxsw2@218.241.178.211/CrawData?driver=SQL+Server+Native+Client+10.0')
def main():
	url ='http://218.56.48.184:8088/socialorg/socExternal/queryPenaltyList.action'
	i=1
	while i==1:
		time.sleep(5)
		data = {'SORG_NAME':'','CREDIT_CODE':'','morgArea':'1','page':'1','rows':'500'}
		html = requests.post(url,data)
		content=html.json()
		total=content['total']/500
		#得到json并传入dataframe
		df = pd.DataFrame(content['rows'])
		df.to_sql('unshandong',engine,if_exists='append',index=False,chunksize=100,dtype ={col_name:sqlalchemy.types.NVARCHAR(length=500) for col_name in df})
		i=i+1
if __name__ == '__main__':
    main()	
