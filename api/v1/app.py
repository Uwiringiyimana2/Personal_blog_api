#!/usr/bin/env python3
from flask import Flask
from api.v1.views import app_views
from flask_cors import CORS
from api.v1.config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r"/api/v1/*": {"origin": "*"}})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5004")
