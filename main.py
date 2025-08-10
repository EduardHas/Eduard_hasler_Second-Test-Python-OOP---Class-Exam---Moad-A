from datetime import datetime
from order_item import OrderItem
from customer import Customer, CustomerType, Gift
from regular_order import RegularOrder
from vip_order import VipOrder
from order import PaymentType

# Creating items
item1 = OrderItem(1, "Laptop", 3000)
item2 = OrderItem(2, "Mouse", 150)
item3 = OrderItem(3, "Keyboard", 400)

# Creating customers
customer1 = Customer(1, "Edi", "Levi", "edi@example.com", "Nof HaGalil", CustomerType.REGULAR)
customer2 = Customer(2, "Dana", "Cohen", "dana@example.com", "Tel Aviv", CustomerType.VIP, discount=0.1)

# Creating a normal order
order1 = RegularOrder(
order_id=101,
name="Edi's Order",
address=customer1.address,
items=[item1, item2],
customer=customer1,
payment_type=PaymentType.CREDIT_CARD,
order_date=datetime.now()
)

# Creating a VIP order
order2 = VipOrder(
order_id=102,
name="Dana's VIP Order",
address=customer2.address,
items=[item1, item3],
customer=customer2,
payment_type=PaymentType.CASH,
order_date=datetime.now()
)

# Printing the details of the orders
print(f"\nOrder #{order1.order_id} Total: ₪{order1.total_price:.2f}")
print(f"Favorites of {customer1.first_name}: {[item.name for item in customer1.favorite_items]}")

print(f"\nOrder #{order2.order_id} Total: ₪{order2.total_price:.2f}")
print(f"Favorites of {customer2.first_name}: {[item.name for item in customer2.favorite_items]}")

# A gift to a customer
gift = Gift()
customer2.take_gift(gift)
customer2.open_gift()



# Creating a VIP customer with a discount
vip = Customer(1, "Edi", "Cohen", "edi@example.com", "Nof HaGalil", CustomerType.VIP, discount=0.1)

# Creating items
item1 = OrderItem("Laptop", 3000)
item2 = OrderItem("Mouse", 150)

# Creating a VIP order
order = VipOrder(
    order_id=1,
    name="Edi's VIP Order",
    address=vip.address,
    items=[item1, item2],
    customer=vip,
    payment_type=PaymentType.CREDIT_CARD,
    order_date=datetime.now()
)
# Processing the VIP order
order.process_order()

print("Total price after discount:", order.total_price)