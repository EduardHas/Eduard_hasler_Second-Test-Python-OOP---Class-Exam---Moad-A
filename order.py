from abc import ABC, abstractmethod
import datetime
from order_item import OrderItem
from customer import Customer, CustomerType
from order_registry import OrderRegistry  # Unique mechanism for orders


class Order(ABC):
        _id_counter = 1  # Static variable to keep track of the last used ID
        def __init__(self, order_id: int, name: str, address: str, items: list[OrderItem],
                     customer: Customer, payment_type: str, order_date: datetime):
            # Check for uniqueness of order_id
            OrderRegistry.register_order_id(order_id)
            self.order_id = order_id
            self.name = name
            self.address = address
            self.items = items
            self.customer = customer
            self.payment_type = payment_type
            self.order_date = order_date
            self.total_price = self._calculate_total_price()
            self._update_favorites()
            Order._id_counter += 1

        def add_item(self, item: OrderItem):
            self.items.append(item)
            self._update_favorites()
            self.total_price = self._calculate_total_price()

        def _update_favorites(self):
            for item in self.items:
                self.customer.add_favorite_item(item)

        @abstractmethod
        def _calculate_total_price(self):
            """Abstract method to calculate the total price of the order."""
            pass

class PaymentType:
    CREDIT_CARD = "Credit Card"
    CASH = "Cash"
    CHECK = "Check"
    OTHER = "Other"







