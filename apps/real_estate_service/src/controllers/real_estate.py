import re
from flask import Blueprint, request

from src.models.real_estate import RealEstate, KindRealEstate
from src.database import db

real_estate_route = Blueprint(
    'real_estate', __name__, url_prefix='/api/v1/real_estate')


@real_estate_route.get('/')
def get_real_estate_by_city() -> str:
    real_estate = RealEstate.query.all()
    return real_estate


@real_estate_route.post('/')
def add_real_estate():
    new_real_estate = RealEstate(
        owner_id=request.json['owner_id'],
        name=request.json['name'],
        kind=KindRealEstate[request.json['kind']],
        description=request.json['description'],
        city=request.json['city'],
        surface=request.json['surface'])

    db.session.add(new_real_estate)
    db.session.commit()

    return new_real_estate.to_JSON()


@real_estate_route.get('<id>')
def get_real_estate_(id):
    real_estate = RealEstate.query.get(id)
    if real_estate:
        return real_estate.to_JSON(), 201
    else:
        raise Exception("Real Estate not exist")


@real_estate_route.patch('<id>')
def edit_real_estate(id):
    real_estate = RealEstate.query.get(id)

    if real_estate is None:
        raise Exception("Real estate not found")

    real_estate.name = "EDIT NAME"
    db.session.commit()

    return real_estate.to_JSON()


@real_estate_route.delete('<id>')
def remove_real_estate(id):
    real_estate = RealEstate.query.get(id)
    if real_estate is None:
        raise Exception("Real estate not found")

    db.session.delete(real_estate)
    db.session.commit()

    return {
        "status_code": 204,
        "message": "Real estate was successfully deleted"
    }, 204
