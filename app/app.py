from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from services.security import authenticate, identity
from resources.user import UserRegisterAPI
from resources.item import ItemAPI, ItemListAPI
from resources.store import StoreAPI, StoreListAPI

app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "thisisavaryscretkey"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(StoreAPI, "/stores/<string:name>")
api.add_resource(StoreListAPI, "/stores")
api.add_resource(ItemAPI, "/items/<string:name>")
api.add_resource(ItemListAPI, "/items")
api.add_resource(UserRegisterAPI, "/register")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
