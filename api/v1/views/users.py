#!/usr/bin/env python3
"""users route"""
from datetime import datetime, timedelta
from api.v1.views import app_views
from models.user import User
from models.db import DB
from flask import request, jsonify
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import jwt
from api.v1.config import Config
from functools import wraps


db = DB()
SECRET_KEY = Config.SECRET_KEY


def token_required(f):
    """ verify token """
    @wraps(f)
    def decorated(*args, **kwargs):
        """decorator"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers.get('x-access-token')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = db.find_user_by(email=data['email'])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401
        except:
            return jsonify({"message": str(e)}), 401
        return f(current_user, *args, **kwargs)
    return decorated


def _hash_password(password):
    """ generate hashed password"""
    encode_pw = password.encode("utf-8")
    return bcrypt.hashpw(encode_pw, bcrypt.gensalt())


@app_views.route("/signup", methods=["POST"], strict_slashes=False)
def signup():
    """ create user """
    email = request.form.get("email")
    firstName = request.form.get("firstname")
    lastName = request.form.get("lastname")
    password = request.form.get("password")
    hash_pw = _hash_password(password)
    try:
        user = db.find_user_by(email=email)
        if user:
            return jsonify({"message": "Already signed Up!"})
    except NoResultFound:
        user = None
    try:
        user = User(email=email, firstName=firstName, lastName=lastName, password=hash_pw)
        if user:
            db.new(user)
            db.save()
            return jsonify({"message" : "Successful signed in"})
    except Exception as e:
        return jsonify({"Failed to create User": f"{e}"})


@app_views.route("/login", methods=["POST"], strict_slashes=False)
def login():
    """ login and create token """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"message": "Login required!"}), 401
    try:
        user = db.find_user_by(email=email)
    except NoResultFound:
       return  jsonify({"message": "User not found!"}), 404
    if bcrypt.checkpw(password.encode("utf-8"), user.password):
        token = jwt.encode({'email': user.email, 'exp': datetime.utcnow() + timedelta(minutes=10)}, SECRET_KEY)
        return jsonify({"token": token})
    else:
        return jsonify({"message": "Invalid credentials"}), 401
