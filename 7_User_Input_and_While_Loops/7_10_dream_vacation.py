# 7-10. Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

prompt = "If you could visit one place in the world, where "
prompt += "would you go? "

responses = {}

poll_active = True
while poll_active:
    name = input("\nWhat is your name? ")
    response = input(prompt)

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        poll_active = False
    
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response}.")
