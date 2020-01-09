#! /usr/bin/python3
# -*- coding:utf-8 -*-
# 文件使用了最基本的flask-restful 实现基本的restful 接口
from flask_restful import Resource,reqparse
from flask.blueprints import Blueprint
order_bp = Blueprint('order_bp',__name__,url_prefix='/orders')
parser = reqparse.RequestParser()

class OrderList(Resource):

    def get(self):
        parser.add_argument('rate', type=int, help='xxxxxxxxxxxxxxx must be int')  # 参数做简单的校验  如果想自定义
        args = parser.parse_args()
        print(args)
        return 'order'


class Order(Resource):

    def post(self,order_id):
        '''
        def list_type(value, name):
            if not value:
                return []
            elif not isinstance(value, list):
                raise ValueError(name + '参数类型错误，必须是list类型')
            return value
        #test.add_argument('rd_center_list', type=list_type, required=False, nullable=False, location=['json'])
        自定义参数的校验可以自己定义函数
        type类型有  int , zero_int ,str,empty_str location form , json等
        :param order_id:
        :return:
        '''
        parser.add_argument('rate',type=int,help='xxxxxxxxxxxxxxx must be int')  #参数做简单的校验  如果想自定义
        args = parser.parse_args()
        print(args)
        return order_id




