#!/usr/bin/python3
"""a new view for State objects"""
from flask import jsonify, abort, request
from api.v1.views import app_views

@app_views.routes('/state', methods=['GET'])
def get_state():
    """returning all states"""
    States = State.all()
    retun jsonify([State.to_dict() for State in States])

@app_views.routes('/state/<int:id>', methods=['GET'])
def get_state(id):
    """retriving state basing on id"""
    St = state.get(id)
    if st is None:
        return(404)
    return jsonify(st.to_dict())

