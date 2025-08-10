from enum import Enum

class CustomerType(Enum):
    REGULAR = "Regular"
    VIP = "VIP"

class CustomerRegistry:
    _registered_ids = set()

    @classmethod
    def register_customer_id(cls, customer_id):
        if customer_id in cls._registered_ids:
            raise ValueError(f"Customer ID {customer_id} already exists.")
        cls._registered_ids.add(customer_id)

class Gift:
    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")

class Customer:
    def __init__(self, customer_id:int, first_name: str, last_name: str,
                 email: str, address: str, customer_type: CustomerType,
                 discount: float = 0.0):
        CustomerRegistry.register_customer_id(customer_id)
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.customer_type = customer_type
        self.discount = discount
        self.favorite_items = []
        self.gift: Gift | None = None

    def add_favorite_item(self, item):
        if item.name not in [i.name for i in self.favorite_items]:
            self.favorite_items.append(item)

    def get_discount(self):
        return self.discount

    def take_gift(self, gift: Gift):
        self.gift = gift

    def open_gift(self):
        if self.gift:
            self.gift.open_gift()
        else:
            print("No gift to open.")