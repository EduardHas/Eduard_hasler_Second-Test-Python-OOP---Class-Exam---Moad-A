from order import Order
from customer import CustomerType
from customer import Customer
from overrides import overrides


class VipOrder(Order):
    def __init__(self, order_id: int, name: str, address: str, items: list,
                 customer: Customer, payment_type: str, order_date):
        super().__init__(order_id, name, address, items, customer, payment_type, order_date)
        self.order_type = "VIP"
    @overrides
    def _calculate_total_price(self):
        base_price = sum(item.price for item in self.items)
        discount = self.customer.get_discount() if hasattr(self.customer, 'get_discount') else 0
        return base_price * (1 - discount)

    def process_order(self):
        print(f"Processing VIP order #{self.order_id} for {self.customer.first_name}")
        if self.customer.customer_type != CustomerType.VIP:
            raise ValueError("Cannot process VIP order for non-VIP customer.")