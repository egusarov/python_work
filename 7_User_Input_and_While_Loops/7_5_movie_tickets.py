# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

prompt = "\nPlease enter your age for a ticket price:"
prompt += "\n(Please enter 'quit' when you finished.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            ticket = 0
            print(f"\nYour movie ticket is free.")
            continue
        elif age < 12:
            ticket = 10
        else:
            ticket = 15
        print(f"\nYour movie ticket costs ${ticket}.")