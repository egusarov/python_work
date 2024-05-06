# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nPlease enter your age for a ticket price:"
prompt += "\n(Please enter 'quit' when you finished.) "

# Use an active variable to control how long the loop runs.
active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
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
