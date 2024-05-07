# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
# Randomly select 4 numbers or letters from the list and 
# print a message saying that any ticket matching these 4 numbers or letters wins a prize.


from random import choice


tickets = ['a', 'b', 'c', 'd', 'e', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

winner_ticket = []
for i in range(4):
    number = choice(tickets)
    winner_ticket.append(number)

print(f"Any ticket matching these 4 numbers or letters {winner_ticket} wins a prize.")