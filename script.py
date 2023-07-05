
#1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olive", "anchovies", "mushrooms"]
#2
prices = [2, 6, 1, 3, 2, 7, 2]
#3
print(prices.count(2))
#4
num_pizzas = len(toppings)
#5
print("We sell " + str(num_pizzas) + " different kind of pizza!")
#6
pizza_and_prices=[[prices[0],toppings[0]],[prices[1],toppings[1]],[prices[2],toppings[2]],[prices[3],toppings[3]],[prices[4],toppings[4]],[prices[5],toppings[5]],[prices[6],toppings[6]]]
#7
print(pizza_and_prices)
# pizzas = list(zip(toppings, prices))
# print(pizzas)
#8
#pizza.sort()
#9
cheapest_pizza = pizza_and_prices[0]
#10
priciest_pizza = pizza_and_prices[0]
#11
pizza_and_prices.pop()

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
# num_two_dollar_slices = prices.count(2)
# print(num_two_dollar_slices)
