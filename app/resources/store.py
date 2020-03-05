from flask_restful import Resource, reqparse
from models.store import Store


class StoreAPI(Resource):
    def get(self, name):
        store = Store.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def delete(self, name):
        store = Store.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store deleted"}, 200


class StoreListAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, help="This field cannot be blank.")

    def post(self):
        data = StoreListAPI.parser.parse_args()
        store = Store.find_by_name(data["name"])
        if store:
            return {"message": "Store already exists."}, 400
        store = Store(**data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred creating the store"}, 500
        return store.json(), 200

    def get(self):
        return {"stores": [store.json() for store in Store.query.all()]}
