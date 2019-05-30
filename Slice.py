
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell ", num_pizzas, " different kids of pizzas!")

pizzas = list(zip(toppings, prices))
print(pizzas)


def take_second(elem):
    return elem[1]


pizzas.sort(key=take_second)
print(pizzas)

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)

num_two_dollar_prices = prices.count(2)
print(num_two_dollar_prices)