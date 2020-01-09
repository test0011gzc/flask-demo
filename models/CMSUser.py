from manage import db
from datetime import datetime

class CMSUser(db.Model):
    __tablename__ = "cms_user"
    # db.Column表示是数据库真实存在的字段, primary_key表示为主键, autoincrement表示自动增长, 每次加1
    # Integer是整形
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # String字符串 长度50个字符
    # nullable	如果为True，允许有空值，如果为False，不允许有空值
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    # unique 如果为True，代表这列不允许出现重复的值
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)