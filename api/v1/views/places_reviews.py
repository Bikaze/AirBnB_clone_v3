#!/usr/bin/python3
"""This route returns json status response implementing places_reviews"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'],
                 strict_slashes=False)
def reviews_per_place(place_id=None):
    """reviews route to handle http method for requested reviews by place"""
    place_obj = storage.get('Place', place_id)

    if request.method == 'GET':
        if place_obj is None:
            abort(404, 'Not found')
        all_reviews = storage.all('Review')
        place_reviews = [obj.to_dict() for obj in all_reviews.values()
                         if obj.place_id == place_id]
        return jsonify(place_reviews)

    if request.method == 'POST':
        if place_obj is None:
            abort(404, 'Not found')
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        user_id = req_json.get("user_id")
        if user_id is None:
            abort(400, 'Missing user_id')
        user_obj = storage.get('User', user_id)
        if user_obj is None:
            abort(404, 'Not found')
        if req_json.get('text') is None:
            abort(400, 'Missing text')
        req_json['place_id'] = place_id
        new_object = Review(**req_json)
        new_object.save()
        return jsonify(new_object.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def reviews_with_id(review_id=None):
    """reviews route to handle http methods for given review by ID"""
    review_obj = storage.get('Review', review_id)

    if request.method == 'GET':
        if review_obj is None:
            abort(404, 'Not found')
        return jsonify(review_obj.to_dict())

    if request.method == 'DELETE':
        if review_obj is None:
            abort(404, 'Not found')
        review_obj.delete()
        del review_obj
        return jsonify({}), 200

    if request.method == 'PUT':
        if review_obj is None:
            abort(404, 'Not found')
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        for key, value in data.items():
            if key not in ['id', 'user_id', 'place_id', 'created_at',
                           'updated_at']:
                setattr(review_obj, key, value)
        storage.save()
        return jsonify(review_obj.to_dict()), 200