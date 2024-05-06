# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again.
#     Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
#     Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe a restaurant in response to a command."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Simulate the restaurant is open."""
        print(f"{self.restaurant_name} restaurant is open.")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers who’ve been served."""
        self.number_served += number

restaurant = Restaurant("McDonald’s", 'Fast Food')

print(f"Restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 50
print(f"Restaurant has served {restaurant.number_served} customers.")

restaurant.set_number_served(75)
print(f"Restaurant has served {restaurant.number_served} customers.")

restaurant.increment_number_served(10)
print(f"Restaurant has served {restaurant.number_served} customers.")