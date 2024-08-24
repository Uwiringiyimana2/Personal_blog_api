#!/usr/bin/env python3
from flask import jsonify, request
from api.v1.views import app_views
from models.db import DB
from models.blog import Blog
from api.v1.views.users import token_required


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
def home_blog(id):
    """Get all published blogs by ID"""
    try:
        blog = db.get(Blog, id)
        if blog:
            return jsonify(blog)
        else:
            abort(404)
    except Exception as e:
        abort(404)


@app_views.route("/blog", methods=['GET'], strict_slashes=False)
@token_required
def get_user_blog(current_user):
    """Get all published blogs by the user"""
    try:
        blogs = db.all_user_blog(current_user.id)
        if blogs:
            return jsonify(blogs)
        else:
            return jsonify([])
    except Exception:
        print(f"Error fetching blogs: {e}")
        abort(404)


@app_views.route("/blog/<int:id>", methods=['GET'], strict_slashes=False)
@token_required
def get_user_blog_by_id(current_user, id):
    """Get all published blog by ID by the user"""
    if current_user is None:
        return jsonify({"message": "Need to login first!"})
    try:
        blog = db.get(Blog, id)
        if blog:
            return jsonify(blog)
        else:
            abort(404)
    except Exception as e:
        abort(404)


@app_views.route("/blog", methods=['POST'], strict_slashes=False)
@token_required
def create_blog(current_user):
    """ POST api/v1/blog
    """
    title = request.form.get("title")
    if not title:
        return jsonify({"Error": "Missing title!"})
    content = request.form.get("content")
    if not content:
        return jsonify({"Error": "Missing content!"})
    try:
        blog = Blog(title=title, content=content, user_id=current_user.id)
        db.new(blog)
        db.save()
    except Exception:
        return jsonify({"message": "Failed to create blog!"})
    return jsonify({"message": "Blog created successful!"})


@app_views.route("/blog/<int:id>", methods=['PUT'], strict_slashes=False)
@token_required
def update_blog(current_user, id):
    """ PUT /api/v1/blog/:id
    """
    title = request.form.get("title")
    content = request.form.get("content")
    try:
        blog = 
    return ""


@app_views.route("/blog/<int:id>", methods=['DELETE'], strict_slashes=False)
@token_required
def delete_blog(current_user, id):
    """ DELETE /api/v1/blog/:id
    """
    return ""
