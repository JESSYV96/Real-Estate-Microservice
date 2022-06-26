import json
from flask import Blueprint, request

from src.decorators import real_estate_owner
from src.models.real_estate import RealEstate, KindRealEstate
from src.database import db

real_estate_route = Blueprint(
    'real_estate', __name__, url_prefix='/api/v1/real_estate')


@real_estate_route.get('/')
def get_real_estate_by_city():
    real_estate_list = []
    city = request.args.get('city')

    if city:
        real_estate = RealEstate.query.filter_by(city=city).all()
    else:
        real_estate = RealEstate.query.all()

    for real_estate_item in real_estate:
        real_estate_list.append(real_estate_item.to_JSON())

    return json.dumps(real_estate_list)


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


@real_estate_route.put('<real_estate_id>')
@real_estate_owner
def edit_real_estate(real_estate_id):
    real_estate = RealEstate.query.get(real_estate_id)

    if real_estate is None:
        raise Exception("Real estate not found")

    real_estate.name = request.json['name']
    real_estate.kind = KindRealEstate[request.json['kind']]
    real_estate.description = request.json['description']
    real_estate.city = request.json['city']
    real_estate.surface = request.json['surface']

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
    }
