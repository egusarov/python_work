# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

prompt = ("\nPlease enter the pizza toppings you'd like to add:")
prompt += ("\n(Please enter 'quit' when you finished.) ")

pizza_toppings = ""

while pizza_toppings != 'quit':
    pizza_toppings = input(prompt)

    if pizza_toppings != 'quit':
        print(f"\nWe'll add {pizza_toppings} to your pizza.")
