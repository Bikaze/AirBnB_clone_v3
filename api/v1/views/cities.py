#!/usr/bin/python3
"""This is the blueprint for cities"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def state_cities(state_id=None):
    """cities in a state"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)

    if request.method == 'GET':
        all_cities = storage.all('City')
        state_ctys = [obj.to_dict() for obj in all_cities.values()
                      if obj.state_id == state_id]
        return jsonify(state_ctys)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get("name") is None:
            abort(400, 'Missing name')
        req_json['state_id'] = state_id
        new_obj = City(**req_json)
        new_obj.save()
        return jsonify(new_obj.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def cities_with_id(city_id=None):
    """get, update or delete a given city"""
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(city_obj.to_dict())

    if request.method == 'DELETE':
        storage.delete(city_obj)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        for key, value in req_json.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(city_obj, key, value)
        city_obj.save()
        return jsonify(city_obj.to_dict()), 200
