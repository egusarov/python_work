# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number
# of arguments each time.


def make_sandwich(*items):
    print("\nMaking your sandwich with next item(s):")
    for item in items:
        print(f"- {item}")


make_sandwich('chicken')
make_sandwich('ham', 'egg', 'cheese')
make_sandwich('egg', 'cheese')
