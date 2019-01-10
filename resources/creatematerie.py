from db import db
from flask_restful import Resource, request
from flask_jwt import jwt_required

from models.classes import ClassModel, find_by_admin
from models.randomtag import randomtag
from models.users import UserModel, add_to_class

class CreateMaterie(Resource):

    @jwt_required()
    def post(self, name):
        data=request.get_json()
