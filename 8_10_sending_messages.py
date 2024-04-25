# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending a message: {current_message}")
        sent_messages.append(current_message)


def show_messages(items):
    print("\nNext messages have been sent successfully:")
    for item in items:
        print(item)


messages = [
    'Hi there! ...',
    'Thanks for getting in touch! ...',
    'We appreciate you taking the time to reach out to our team. ...',
    ]
sent_messages = []

send_messages(messages, sent_messages)
show_messages(sent_messages)

print("\nCheck that the messages were moved correctly")
print(f"Original list: {messages}")
print(f"New list: {sent_messages}")
