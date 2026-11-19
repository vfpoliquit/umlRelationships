class Customer:

    def __init__(self, name: str):
        self.name = name
        self.orders = []  # Keeps track of linked orders


class Order:

    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer  # Reference link back to Customer
        customer.orders.append(self)


# Usage
alice = Customer("Alice")
order_1 = Order(101, alice)
order_2 = Order(102, alice)

print(f"Customer Profile: {alice.name}")
for o in alice.orders:
    print(f"  Order ID: {o.order_id}")

print(f"Order #101 lookup -> Owned by customer: {order_1.customer.name}")