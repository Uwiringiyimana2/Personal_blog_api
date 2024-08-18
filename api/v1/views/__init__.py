#!/usr/bin/env python3
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views import index, users, blogs
# from api.v1.views.blogs import *
# from api.v1.views.users import *
