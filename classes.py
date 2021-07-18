import uuid


class Item:
    def __init__(self, name, price):
        self.id = uuid.uuid4().hex
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: {self.price}$ -- {self.id}"


class Book(Item):
    def __init__(self):
        super().__init__(name="Book", price=15)


class CoffeeMachine(Item):
    def __init__(self):
        super().__init__(name="CoffeeMachine", price=100)


class SoccerBall(Item):
    def __init__(self):
        super().__init__(name="SoccerBall", price=25)


class Candle(Item):
    def __init__(self):
        super().__init__(name="Candle", price=5)


class Customer:
    def __init__(self, name):
        self.id = uuid.uuid1()
        self.name = name
        self.cart = []
        self.balance = 0
        self.money_spent = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError(f"Not enough funds! {amount} > {self.balance}")
        self.balance -= amount

    def __repr__(self):
        return f"Name: {self.name}, Balance: {self.balance}$, Money Spent: {self.money_spent}$"


class Amazon:
    def __init__(self):
        self.customers = {}

    def create_account(self, name):
        cust = Customer(name)
        self.customers[cust.id] = cust
        return cust.id

    def delete_account(self, customer_id):
        del(self.customers[customer_id])

    def add_to_cart(self, customer_id, item):
        cust = self._get_cust(customer_id)
        cust.cart.append(item)

    def remove_from_cart(self, customer_id, item):
        cust = self._get_cust(customer_id)
        if item in cust.cart:
            cust.cart.remove(item)
            return item
        return None

    def buy_item(self, customer_id, item):
        cust = self._get_cust(customer_id)
        if item not in cust.cart:
            raise ValueError(f"Customer cart does not contain {item}")
        if item.price > cust.balance:
            raise ValueError(f"Customer does not have sufficient funds to purchase {item}")
        cust.balance -= item.price
        cust.money_spent += item.price
        self.remove_from_cart(cust.id, item)

    def buy_entire_cart(self, customer_id):
        cust = self._get_cust(customer_id)
        total_cost = 0
        for item in cust.cart:
            total_cost += item.price
        if len(cust.cart) >= 3:
            total_cost *= 0.9
        if cust.balance < total_cost:
            raise ValueError("Customer does not have sufficient funds!")
        cust.balance -= total_cost
        cust.money_spent += total_cost

    def clear_cart(self, customer_id):
        cust = self._get_cust(customer_id)
        cust.cart = []

    def show_cart(self, customer_id):
        cust = self._get_cust(customer_id)
        print(f"Total # of items {len(cust.cart)}")
        books = 0
        candles = 0
        coffee_machines = 0
        soccer_balls = 0
        for item in cust.cart:
            if isinstance(item, Book):
                books += 1
            elif isinstance(item, Candle):
                candles += 1
            elif isinstance(item, CoffeeMachine):
                coffee_machines += 1
            elif isinstance(item, SoccerBall):
                soccer_balls += 1
        print(f"Total # of books: {books}")
        print(f"Total # of candles: {candles}")
        print(f"Total # of coffee machines: {coffee_machines}")
        print(f"Total # of soccer balls: {soccer_balls}")
        print("Cart contents:")
        for item in cust.cart:
            print(item)

    def _get_cust(self, customer_id):
        if customer_id not in self.customers:
            raise ValueError(f"Customer with id {customer_id} does not exist...")
        return self.customers[customer_id]



