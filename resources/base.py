from flask_restful import Resource
class Base (Resources):
    def get(self):
        return "benvenuti nell'api di matteo il re della doppietta"
