class Config(object):
    DEBUG = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'nfoiqwtcbasdkhsa'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://cfc:!QAZxsw2@218.241.178.211/CrawData?driver=SQL+Server+Native+Client+10.0"
