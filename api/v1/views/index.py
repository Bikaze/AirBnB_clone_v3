#!/usr/bin/python3
"""Returning the status of the api"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """handles the status route"""
    return jsonify({"status": "OK"})
