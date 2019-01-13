from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.register import Register
from security import identity, authenticate
from resources.createclass import CreateClass
from resources.joinclass import JoinClass
from resources.friend import Friend
from resources.tag import Tag
from resources.base import Base
from resources.makeadmin import MakeAdmin
from resources.mates import Mates
from resources.isadmin import IsAdmin
from resources.gotmate import GotMate
from resources.createsubject import CreateSubject
from resources.createorario import CreateOrario

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.secret_key="Matteo"
api=Api(app)






jwt = JWT (app, authenticate, identity)
app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
#app.config['JWT_EXPIRATION_DELTA'] =seconds=1800000

@app.before_first_request
def create_table():
    db.create_all()





api.add_resource(Register, "/register")
api.add_resource(CreateClass, "/class/create")
#api.add_resource(CreateMaterie, "/creatematerie/<string:name>")
api.add_resource(JoinClass, "/class/join")
api.add_resource(Friend, "/user/friend")
api.add_resource(Tag, "/class/tag")
#api.add_resource(Base, "/")
api.add_resource(MakeAdmin, "/class/admin")
api.add_resource(Mates, "/class/mates")
api.add_resource(IsAdmin, "/user/isadmin")
api.add_resource(GotMate, "/user/gotmate")

api.add_resource(CreateSubject, "/subject/create")
api.add_resource(CreateOrario, "/timetable/create")



if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
