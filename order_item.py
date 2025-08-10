class ItemRegistry:
    _registered_ids = set()

    @classmethod
    def register_item_id(cls, item_id):
        if item_id in cls._registered_ids:
            raise ValueError(f"Item ID {item_id} already exists.")
        cls._registered_ids.add(item_id)

class OrderItem:
    def __init__(self, item_id: int, name: str, price: float):
        ItemRegistry.register_item_id(item_id)
        self.item_id = item_id
        self.name = name
        self.price = price