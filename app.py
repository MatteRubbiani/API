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

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"]=False
app.secret_key="Matteo"
api=Api(app)






jwt = JWT (app, authenticate, identity)
app.config['JWT_AUTH_USERNAME_KEY'] = 'mail'
#app.config['JWT_EXPIRATION_DELTA'] =seconds=1800000




api.add_resource(Register, "/register")
api.add_resource(CreateClass, "/class/create")
#api.add_resource(CreateMaterie, "/creatematerie/<string:name>")
api.add_resource(JoinClass, "/class/join")
api.add_resource(Friend, "/user/friend")
api.add_resource(Tag, "/class/tag")
api.add_resource(Base, "/")



if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
