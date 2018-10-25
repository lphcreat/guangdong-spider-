#初始化表

from sqlalchemy import Column, String, create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('mssql+pyodbc://......./CrawData?driver=SQL+Server+Native+Client+10.0')
# 创建DBSession类型:
# 定义User对象:
class Table(Base):
    # 表的名字:
    __tablename__ ='mes_guangdongss'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    credit_num = Column(String(500))
    re_num=Column(String(500))
    or_name=Column(String(500))
    or_type=Column(String(500))
    or_date=Column(String(500))
    manager=Column(String(500))
    person=Column(String(500))
    address=Column(String(500))
    #city=Column(String(500))
    #Base.metadata.create_all(engine)
    pass

if __name__ == '__main__':
    Base.metadata.create_all(engine)
