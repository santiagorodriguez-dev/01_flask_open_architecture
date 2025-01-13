from app.extensions import db
from flask_restful import Api # type: ignore
from flask import Flask # type: ignore
from app.routes import HelloWorld, ItemList, ItemDetail

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    api = Api(app)
    db.init_app(app)

    api.add_resource(HelloWorld, '/')
    api.add_resource(ItemList, '/items')
    api.add_resource(ItemDetail, '/item/<int:item_id>')
    return app