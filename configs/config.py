import sys
import os


class Default(object):

    DEBUG = True
    ROOT_PATH =BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_URL_PATH = os.path.join(BaseDir, 'static')
    TEMPLATE_FOLDER = os.path.join(BaseDir, 'templates')
    SECRET_KEY = '21fsdfs'
    #SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/test?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = True