from flask import Flask
from configs.config import Default
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from regex import RegexConverter
import api as flask_api

__all__ = ['app','db','manager']

#todo 创建app对象
def create_app():
    app = Flask(__name__)
    app.config.from_object(Default()) #配置app的配置
    return app

app = create_app()
app.url_map.converters['regex'] = RegexConverter   #让app的所有路由都支持正则表达式
db = SQLAlchemy(app) #初始化db
migrate = Migrate(db=db) #使用插件来管理db
migrate.init_app(app) #插件初始化app
manager = Manager(app) # 注册管理app的插件

#todo 注册蓝图
app.register_blueprint(flask_api.user_bp,url_prefix=flask_api.user_bp.url_prefix)
app.register_blueprint(flask_api.order_bp,url_prefix=flask_api.order_bp.url_prefix)

#其他



