#!/usr/bin/python3
"""This is the Flask App to make the HBnB(AirBnB clone) alive"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

HOST = os.getenv('HBNB_API_HOST', '0.0.0.0')
PORT = os.getenv('HBNB_API_PORT', 5000)

app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "Not a JSON"}), 400)


@app.teardown_appcontext
def teardownDb(exception):
    """This function closes the SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True)
