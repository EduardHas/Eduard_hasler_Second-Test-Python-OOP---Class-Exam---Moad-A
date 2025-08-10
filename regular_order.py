from overrides import overrides
from datetime import datetime
from order_item import OrderItem
from customer import Customer
from order import Order


class RegularOrder(Order):
    def __init__(self, order_id: int, name: str, address: str, items: list[OrderItem],
                 customer: Customer, payment_type: str, order_date: datetime):
        super().__init__(order_id, name, address, items, customer, payment_type, order_date)
        self.order_type = "Regular"

    @overrides
    def _calculate_total_price(self) -> float:
       return sum(item.price for item in self.items)
    def process_order(self):
     print(f"Processing regular order #{self.order_id} for {self.customer.first_name}")



