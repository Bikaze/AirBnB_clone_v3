#!/usr/bin/python3
"""An end point for usr"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id=None):
    """a function to retrieve user from the database"""
    if state_id is None:
        states = storage.all(State)
        state_list = [state.to_dict() for state in states.values()]
        return jsonify(state_list)
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())
