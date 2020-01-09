from .views import Order,OrderList,order_bp
from flask_restful import Api
api = Api(order_bp)

api.add_resource(OrderList,'/')
api.add_resource(Order,'/<order_id>')




