# 9-1. Restaurant: Make a class called Restaurant.
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class.
# Print the two attributes individually, and then call both methods.


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe a restaurant in response to a command."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Simulate the restaurant is open."""
        print(f"{self.restaurant_name} restaurant is open.")


restaurant = Restaurant("McDonald’s", 'Fast Food')

print(f"Attribute one (restaurant_name) is {restaurant.restaurant_name}.")
print(f"Attribute two (cuisine_type) is {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
