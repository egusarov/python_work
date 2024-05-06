# 8-9. Messages: Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

def show_messages(items):
    for item in items:
        print(item)

messages = [
    'Hi there! ...',
    'Thanks for getting in touch! ...',
    'We appreciate you taking the time to reach out to our team. ...',
    ]
show_messages(messages)
