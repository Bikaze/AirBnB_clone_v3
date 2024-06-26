#!/usr/bin/python3
"""Returning the status of the api"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """handles the status route"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_starts():
    """retrieving the number of each objects by type"""
    return jsonify(
        {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
        })
