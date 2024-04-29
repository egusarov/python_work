# 9-3. Users: Make a class called User.
# Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.


class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, marital_status):
        """Initialize first and last name, age and marital status."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marital_status = marital_status
        self.full_name = f"{self.first_name} {self.last_name}"

    def describe_user(self):
        """Print a summary of the user’s information."""
        print(
            f"{self.full_name.title()} is {self.age} years old, {self.marital_status}."
        )

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello {self.full_name.title()}, welcome to the party!")


user_1 = User('cillian', 'murphy', 47, 'married')
user_2 = User('paul', 'anderson', 50, 'divorced')
user_3 = User('joseph michael', 'cole', 36, 'single')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()