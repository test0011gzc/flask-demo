from .views import user_bp,User,Users

user_bp.add_url_rule(
    '/',view_func=Users.as_view("users"),
)
user_bp.add_url_rule(
    '/<string:id>',view_func=User.as_view("user"),
)

# user_bp.add_url_rule(
#     '/<regex("\d+"):id>',view_func=User.as_view("user"),
# )

