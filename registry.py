from order import Order

class OrderRegistry:
    def __init__(self):
        self.orders: list[Order] = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def get_all_orders(self) -> list[Order]:
        return self.orders