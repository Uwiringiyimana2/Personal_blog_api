#!/usr/bin/env python3
from flask import jsonify, abort
from api.v1.views import app_views
from models.db import DB
from models.blog import Blog


db = DB()


@app_views.route("/home/blog", methods=['GET'], strict_slashes=False)
def home():
    """home page displaying all published blogs"""
    try:
        blogs = db.all(Blog)
        if blogs:
            return jsonify(blogs)
        else:
            return jsonify([])
    except Exception:
        print(f"Error fetching blogs: {e}")
        abort(404)

@app_views.route("/home/blog/<int:id>", methods=['GET'], strict_slashes=False)
def home_blog():
    try:
        blog = db.get(Blog, id)
        if blog:
            return jsonify(blog)
        else:
            abort(404)
    except Exception:
        print(f"Error fetching blog with id {id}: {e}")
        abort(404)