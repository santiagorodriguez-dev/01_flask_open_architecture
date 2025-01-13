from flask_restful import Resource # type: ignore
from app.extensions import db
from flask import request, jsonify # type: ignore
from app.models import Item

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ItemList(Resource):
        def get(self):
            try:
                items = Item.query.all()
            except:
                 return {"error": "Item not found"}, 404
            if not items:
                return {"error": "Item not found"}, 404
            
            return jsonify([item.to_dict() for item in items])
        
        def post(self):
            data = request.get_json()
            new_item = Item(name=data['name'], price=data['price'])
            print(new_item.to_dict())
            db.session.add(new_item)
            db.session.commit()

            return new_item.to_dict(), 201
        
class ItemDetail(Resource):
    def put(self, item_id):
        item = Item.query.get(item_id)

        if not item:
            return {"error": "Item not found"}, 404
        
        data = request.get_json()
        item.name = data['name']
        item.price = data['price']

        db.session.commit()

        return jsonify(item.to_dict())
    
    def delete(self, item_id):
        item = Item.query.get(item_id)

        if not item:
            return {"error": "Item not found"}, 404
        
        db.session.delete(item)
        db.session.commit()
        
        return {"message": "Item deleted"}, 200