from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import Item


class ItemAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "store_id", type=int, required=True, help="Every item needs a store_id."
    )

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        if item:
            return item.json()

    def post(self, name):
        if Item.find_by_name(name):
            return {"message": "Item already exists."}, 400
        data = ItemAPI.parser.parse_args()
        item = Item(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500
        return item.json(), 201

    def delete(self, name):
        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item has been deleted."}, 200

    def put(self, name):
        data = ItemAPI.parser.parse_args()
        item = Item.find_by_name(name)
        if item:
            item.price = data["price"]
        else:
            item = Item(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred saving the item"}, 500
        return item.json(), 200


class ItemListAPI(Resource):
    def get(self):
        return {"items": [item.json() for item in Item.query.all()]}

