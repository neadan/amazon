import unittest

from classes import Customer, Amazon, Book, CoffeeMachine


class TestCustomer(unittest.TestCase):

    def setUp(self):
        pass

    def test_deposit(self):
        cust = Customer("Sarah")
        self.assertEqual(cust.balance, 0)
        cust.deposit(1000)  # This is where we call the method to test
        self.assertEqual(cust.balance, 1000)

    def test_withdraw_success(self):
        cust = Customer("Sarah")
        cust.balance = 1000
        cust.withdraw(523)
        self.assertEqual(cust.balance, 477)

    def test_withdraw_error(self):
        cust = Customer("Sarah")
        cust.balance = 500
        self.assertRaises(ValueError, cust.withdraw, 501)


class TestAmazon(unittest.TestCase):
    # Assume customer exists in dictionary for all tests!!!

    def setUp(self):
        self.amazon = Amazon()
        self.daniel_id = self.amazon.create_account("Daniel")
        self.daniel_cust = self.amazon.customers[self.daniel_id]
        self.book = Book()
        self.coffee_machine = CoffeeMachine()

    def test_create_account(self):
        if self.daniel_id not in self.amazon.customers:
            self.fail(f"{self.daniel_id} not in customers dict")

    def test_delete_account(self):
        self.amazon.delete_account(self.daniel_id)
        if self.daniel_id in self.amazon.customers:
            self.fail(f"{self.daniel_id} should have been deleted")

    def test_add_to_cart(self):
        self.amazon.add_to_cart(self.daniel_id, self.book)
        if self.book not in self.daniel_cust.cart:
            self.fail(f"{self.book} should be in {self.daniel_cust.cart}")

    def test_remove_from_cart(self):
        self.daniel_cust.cart.append(self.book)
        returned_book = self.amazon.remove_from_cart(self.daniel_id, self.book)
        if self.book in self.daniel_cust.cart:
            self.fail(f"{self.book} should not be in {self.daniel_cust.cart}")
        self.assertEqual(self.book, returned_book)

    def test_remove_from_cart_None(self):
        returned_book = self.amazon.remove_from_cart(self.daniel_id, self.book)
        self.assertEqual(returned_book, None)

    def test_buy_item_error_cart(self):
        self.assertRaises(ValueError, self.amazon.buy_item, self.daniel_id, self.coffee_machine)

    def test_buy_item_error_price(self):
        self.daniel_cust.balance = 99
        self.assertRaises(ValueError, self.amazon.buy_item, self.daniel_id, self.coffee_machine)

    def test_buy_item_success(self):
        self.daniel_cust.cart.append(self.coffee_machine)
        self.daniel_cust.balance = 101
        self.daniel_cust.money_spent = 0
        self.amazon.buy_item(self.daniel_id, self.coffee_machine)
        self.assertEqual(self.daniel_cust.balance, 1)
        self.assertEqual(self.daniel_cust.money_spent, 100)
        if self.coffee_machine in self.daniel_cust.cart:
            self.fail(f"{self.coffee_machine} should not be in {self.daniel_cust.cart}")