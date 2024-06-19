#!/usr/bin/env python3
def add_prices(basket):
    total = 0
    for value in basket.values():
        total += value
    return round(total, 2)
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
print(add_prices(groceries))