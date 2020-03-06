from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from resources.user import UserRegisterAPI
from resources.item import ItemAPI, ItemListAPI
from resources.store import StoreAPI, StoreListAPI

from services.security import authenticate, identity

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
    from services.database import db

    db.init_app(app)

    if app.config["DEBUG"]:

        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000, debug=True)
