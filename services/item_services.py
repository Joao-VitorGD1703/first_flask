from models.item import Item
from repositories.item_repository import ItemRepository

class ItemService:
    def __init__(self):
        self.repository = ItemRepository()

    def get_all_items(self):
        return [item.to_dict() for item in self.repository.get_all()]

    def get_item_by_id(self, item_id):
        item = self.repository.get_by_id(item_id)
        return item.to_dict() if item else None

    def create_item(self, item_data):
        novo_item = Item(len(self.repository.get_all()) + 1, item_data['nome'])
        self.repository.add(novo_item)
        return novo_item.to_dict()
