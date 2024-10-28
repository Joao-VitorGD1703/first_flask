from flask import Blueprint, jsonify, request
from services.item_services import ItemService

item_blueprint = Blueprint('item', __name__)
item_service = ItemService()

@item_blueprint.route('/api/items', methods=['GET'])
def get_items():
    dados = item_service.get_all_items()
    return jsonify(dados)

@item_blueprint.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = item_service.get_item_by_id(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item não encontrado"}), 404

@item_blueprint.route('/api/items', methods=['POST'])
def create_item():
    novo_item = request.json
    created_item = item_service.create_item(novo_item)
    return jsonify(created_item), 201
