import os.path
from flask_restful import Resource
from flask import Flask, Response

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

class ChangePassword (Resource):
    def get (self):
        content = get_file('recuperaPassword.html')
        return Response(content, mimetype="text/html")
