# 8-11. Archived Messages: Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.

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

send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print("\nCheck that the original list has retained its messages")
print(f"Original list: {messages}")
print(f"New list: {sent_messages}")
