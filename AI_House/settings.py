from flask_sqlalchemy import SQLAlchemy
import pymysql

USER = "root"
PASSWORD = "123456zx."
DATABASE = "Train"
HOST = "localhost"
PORT = 3306

pymysql.install_as_MySQLdb()

# 创建FLask-SQLAlchemy的实例对象
db = SQLAlchemy()
class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True