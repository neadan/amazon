# your imports may be different!
from classes import Book, CoffeeMachine, SoccerBall, Candle, Amazon

amazon = Amazon()
john_id = amazon.create_account("John")

candle_1 = Candle()
print(f"Price of a candle is {candle_1.price}")
print("")

amazon.customers[john_id].deposit(candle_1.price)
try:
    amazon.buy_item(john_id, candle_1)  # should throw a ValueError because item not in cart
except ValueError:
    amazon.add_to_cart(john_id, candle_1)
    amazon.buy_item(john_id, candle_1)

print("*****************Part 1*****************")
print("After buying 1 candle:")
print(amazon.customers[john_id])

print("")
print("*****************Part 2*****************")
sarah_id = amazon.create_account("Sarah")
book_1 = Book()  # 15$
book_2 = Book()  # 15$
coffee_1 = CoffeeMachine()  # 100$
coffee_2 = CoffeeMachine()  # 100$
soccer_ball_1 = SoccerBall()  # 25$

total_price = book_1.price + book_2.price + coffee_1.price + coffee_2.price + soccer_ball_1.price

amazon.add_to_cart(sarah_id, book_1)
amazon.add_to_cart(sarah_id, book_2)
amazon.add_to_cart(sarah_id, coffee_1)
amazon.add_to_cart(sarah_id, coffee_2)
amazon.add_to_cart(sarah_id, soccer_ball_1)

amazon.show_cart(sarah_id)

print("")
print("*****************Part 3*****************")

try:
    amazon.buy_entire_cart(sarah_id)  # this should throw a ValueError because not enough funds
except ValueError:
    amazon.customers[sarah_id].deposit(total_price)
    amazon.buy_entire_cart(sarah_id)

print(amazon.customers[sarah_id])

# THE OUTPUT OF THE ABOVE PROGRAM IS:

# Price of a candle is 5
#
# *****************Part 1*****************
# After buying 1 candle:
# Name: John, Balance: 0$, Money Spent: 5$
#
# *****************Part 2*****************
# Total # of items: 5
# Total # of books: 2
# Total # of candles: 0
# Total # of coffee machines: 2
# Total # of soccer balls: 1
# Cart contents:
# Book: 15$ -- 9d47a17c9ed64b9ea41824462368764a
# Book: 15$ -- 7795bdfd127c49e0a36b2ca8292a0542
# Coffee Machine: 100$ -- b531649e06a14b36b96293a9cd897ed5
# Coffee Machine: 100$ -- e5a87b09d1794148a8a96d7fd047e6e3
# Soccer Ball: 25$ -- f8ade4d0f8244612a9a204463294ae42
#
# *****************Part 3*****************
# Name: Sarah, Balance: 25.5$, Money Spent: 229.5$
#
# Process finished with exit code 0
