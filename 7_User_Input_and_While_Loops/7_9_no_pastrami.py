# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = [
    'chicken sandwich', 'pastrami', 'egg sandwich', 'pastrami', 'seafood sandwich',
    'roast beef sandwich', 'grilled cheese', 'pastrami',
    ]

print("Ops! The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"\nAvailable sandwiches: \n{sandwich_orders}")
