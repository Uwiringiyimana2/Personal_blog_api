#!/usr/bin/env python3
from flask import jsonify, abort
from api.v1.views import app_views
from api.v1.auth import basic_auth


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """return sucsess"""
    return jsonify({"status": "OK"})
