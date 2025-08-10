class OrderRegistry:
    _order_ids = set()

    @classmethod
    def register_order_id(cls, order_id: int):
        if order_id in cls._order_ids:
            raise ValueError(f"Order ID {order_id} already exists.")
        cls._order_ids.add(order_id)