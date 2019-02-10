import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager

from resources.register import Register
from security import identity, authenticate
from resources.createclass import CreateClass
from resources.joinclass import JoinClass
from resources.friend import Friend
from resources.tag import Tag
from resources.makeadmin import MakeAdmin
from resources.mates import Mates
from resources.isadmin import IsAdmin
from resources.gotmate import GotMate
from resources.createsubject import CreateSubject
from resources.createorario import CreateOrario
from resources.daytimetable import OrarioGiorno
from resources.put import Put
from resources.confirm_mail import ConfirmMail
from resources.changepsw import ChangePassword
from resources.ConfirmPassword import ConfirmPassword
from resources.finalput import FinalPut
from resources.name import Name
from resources.friendName import FriendName
from resources.authenticate import UserLogin
from resources.classname import ClassName
from resources.admins import Admins


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.config["PROPAGATE_EXCEPTIONS"]=True
app.secret_key="Matteo"
api=Api(app)


jwt = JWTManager (app)
@jwt.user_claims_loader
def add_claims(identity):
    return{"user_id":identity}

#app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=5)

#@app.before_first_request
#def create_table():
    #db.create_all()





api.add_resource(Register, "/register")
api.add_resource(CreateClass, "/class/create")
api.add_resource(JoinClass, "/class/join")
api.add_resource(Friend, "/user/friend")
api.add_resource(Tag, "/class/tag")
api.add_resource(ConfirmMail, "/confirm/<string:token>")
api.add_resource(MakeAdmin, "/class/admin")
api.add_resource(Mates, "/class")
api.add_resource(IsAdmin, "/user/isadmin")
api.add_resource(GotMate, "/user/gotmate")
api.add_resource(CreateSubject, "/subject/create")
api.add_resource(CreateOrario, "/timetable/create")
api.add_resource(OrarioGiorno, "/timetable/day")
api.add_resource(Put, "/friend/put")
api.add_resource(ChangePassword, "/changePassword")
api.add_resource(ConfirmPassword, "/confirmPassword")
api.add_resource(FinalPut, "/final/put")
api.add_resource(Name, "/user/name")
api.add_resource(FriendName, "/user/friend/name")
api.add_resource(UserLogin, "/auth")
api.add_resource(ClassName, "/class/name")
api.add_resource(Admins, "/class/admin/names")



if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
