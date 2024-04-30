#!/usr/bin/python3
"""template for users"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.user import User


@app_views.route('/users/', methods=['GET', 'POST'], strict_slashes=False)
def users_no_id(user_id=None):
    """This route handles requests with no ID given"""
    if request.method == 'GET':
        all_users = storage.all('User')
        all_users = [obj.to_dict() for obj in all_users.values()]
        return jsonify(all_users)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get('email') is None:
            abort(400, 'Missing email')
        if req_json.get('password') is None:
            abort(400, 'Missing password')
        new_object = User(**req_json)
        new_object.save()
        return jsonify(new_object.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def user_with_id(user_id=None):
    """This route handles requests with ID given"""
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(user_obj.to_dict())

    if request.method == 'DELETE':
        user_obj.delete()
        del user_obj
        return jsonify({}), 200

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        for key, value in data.items():
            if key not in ['id', 'email', 'created_at', 'updated_at']:
                setattr(user_obj, key, value)
        user_obj.save()
        return jsonify(user_obj.to_dict()), 200
