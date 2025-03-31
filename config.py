import os
import urllib

class Config:
    TESTING = True

class DevConfig:
    DB_PASSWORD = os.environ['DB_PASSWORD']
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 18 for SQL Server};SERVER=entappa1prdboomisql01.database.windows.net;DATABASE=BoomiLogging;UID=BoomiLoggingProd;PWD=" + DB_PASSWORD)
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://BoomiLoggingProd:" + DB_PASSWORD + "@entappa1prdboomisql01.database.windows.net/BoomiLogging?driver=ODBC+Driver+18+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SECRET_KEY='dev'

class TestConfig:
    DB_PASSWORD = os.environ['DB_PASSWORD']
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 18 for SQL Server};SERVER=entappa1prdboomisql01.database.windows.net;DATABASE=BoomiLogging;UID=BoomiLoggingProd;PWD=" + DB_PASSWORD)
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://BoomiLoggingProd:" + DB_PASSWORD + "@entappa1prdboomisql01.database.windows.net/BoomiLogging?driver=ODBC+Driver+18+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    SECRET_KEY='test'

class ProdConfig:
    DB_PASSWORD = os.environ['DB_PASSWORD']
    params = urllib.parse.quote_plus("DRIVER={ODBC Driver 18 for SQL Server};SERVER=entappa1prdboomisql01.database.windows.net;DATABASE=BoomiLogging;UID=BoomiLoggingProd;PWD=" + DB_PASSWORD)
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://BoomiLoggingProd:" + DB_PASSWORD + "@entappa1prdboomisql01.database.windows.net/BoomiLogging?driver=ODBC+Driver+18+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SECRET_KEY='production'