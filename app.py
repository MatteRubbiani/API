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
from resources.totaltimetable import OrarioTotale
from resources.put import Put
from resources.confirm_mail import ConfirmMail
from resources.changepsw import ChangePassword
from resources.ConfirmPassword import ConfirmPassword
from resources.name import Name
from resources.friendName import FriendName
from resources.authenticate import UserLogin, TokenRefresh
from resources.classname import ClassName
from resources.isInClass import  IsInClass
from resources.removeFromClass import RemoveFromClass
from resources.EliminaUtenti import EliminaUtenti
from resources.subjects import GetSubjects
from resources.GetSubjectsIOS import PutIOS


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL","sqlite:///data.db")
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.config["PROPAGATE_EXCEPTIONS"]=True
app.secret_key="Matteo"
api=Api(app)


jwt = JWTManager (app)


#app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=5)

app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(weeks=100)

#@app.before_first_request
#def create_table():
    #db.create_all()





api.add_resource(Register, "/register")
api.add_resource(CreateClass, "/class/create")
api.add_resource(JoinClass, "/class/join")
api.add_resource(Friend, "/user/friend")
api.add_resource(Tag, "/class/tag")
api.add_resource(ConfirmMail, "/confirm/<string:token>")
api.add_resource(MakeAdmin, "/user/admin")
api.add_resource(Mates, "/class")
api.add_resource(IsAdmin, "/user/isadmin")
api.add_resource(GotMate, "/user/gotmate")
api.add_resource(CreateSubject, "/subject/create")
api.add_resource(CreateOrario, "/timetable/create")
api.add_resource(OrarioTotale, "/timetable/day")
api.add_resource(Put, "/friend/put")
api.add_resource(ChangePassword, "/changePassword")
api.add_resource(ConfirmPassword, "/confirmPassword")
api.add_resource(Name, "/user/name")
api.add_resource(FriendName, "/user/friend/name")
api.add_resource(UserLogin, "/auth")
api.add_resource(ClassName, "/class/name")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(IsInClass, "/user/hasclass")
api.add_resource(RemoveFromClass, "/user/remove/class")
api.add_resource(EliminaUtenti, "/user/remove/all")
api.add_resource(GetSubjects, "/subject")
api.add_resource(PutIOS, "/friend/put/ios")



if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
