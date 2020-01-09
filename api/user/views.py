#! /usr/bin/python3
# -*- coding:utf-8 -*-
# 文件使用了最基本的flask MethodView 实现了基本的restful


from flask.blueprints import Blueprint
from flask.views import MethodView

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')


class Users(MethodView):

    def get(self):
        '''
        获取所有用户
        :return:
        '''
        return 'user_list'


class User(MethodView):

    def get(self,id):
        '''
        通过id 获取单个用户
        :param id:
        :return:
        '''
        print(id)
        return str(id)
