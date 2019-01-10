from flask_restful import Resource
class Base (Resource):
    def get(self):
        return "benvenuti nell'api di matteo il re della doppietta"
