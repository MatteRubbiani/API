from flask_restful import Api
from flask import Flask

from get_number import GetNumber

app = Flask(__name__)
app.secret_key = "Matteo"
api = Api(app)

api.add_resource(GetNumber, "/main")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
