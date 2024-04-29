# 9-2. Three Restaurants: Start with your class from Exercise 9-1.
# Create three different instances from the class, and call describe_restaurant() for each instance.

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


restaurant_1 = Restaurant("McDonald’s", 'Fast Food')
restaurant_2 = Restaurant('Chipotle Mexican Grill', 'Fast Casual')
restaurant_3 = Restaurant('Osteria Francescana', 'Fine Dining')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()