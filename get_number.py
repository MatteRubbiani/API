from flask_restful import Resource, reqparse
from preprocessing_1 import find_array as find_array_1
from preprocessing import find_array
from PIL import Image


class GetNumber(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        data = self.parser.parse_args()
        im = data["image"]
        im = im.convert("RGB")

        a = len(find_array(im))
        b = len(find_array_1(im))
        mean = (a + b) / 2
        return mean
