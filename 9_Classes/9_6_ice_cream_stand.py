# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.


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


class IceCreamStand(Restaurant):
    """An ice cream stand is a specific kind of restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ['chocolate', 'gum', 'vanilla', 'strawberry']

    def describe_flavors(self):
        """Displays flavors."""
        print("\nHere is a list of available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


restaurant = IceCreamStand("McDonald’s", 'Fast Food')
restaurant.describe_flavors()