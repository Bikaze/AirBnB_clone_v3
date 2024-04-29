#!/usr/bin/python3
"""Returning the status of the api"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """handles the status route"""
    return jsonify({"status": "OK"})


@app.route('/api/v1/stats')
def numbers():
    """retrieving the number of each objects by type"""
    objects_count = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonfy(objects_count)
