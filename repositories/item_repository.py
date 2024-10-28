import models.item import item

class ItemRepository:
    def __init__(self):
        self.dados=[
            Item(1, "Item 1"),
            Item(2, "Item 2")
        ]

    def ger_all(self):
        return self.dados

    def get_by_id(self, item_id)
        return next((item for item in self.dados if item.id == item_id), None)


    def add(self, item):
        self.dados.append(item)