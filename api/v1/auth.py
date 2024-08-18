#!/usr/bin/env python3
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from models.db import DB
import bcrypt
import jwt


db = DB()


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(email, password):
    try:
        user = db.find_user_by(email=email)
        if user and bcrypt.checkpw(
            password.encode('utf-8'),
            user.password.encode('utf-8')
        ):
            return user
    except Exception as e:
        print(f"Error verifying password: {e}")
    return None



