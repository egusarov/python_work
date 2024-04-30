# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.


class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, marital_status):
        """Initialize first and last name, age and marital status."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marital_status = marital_status
        self.full_name = f"{self.first_name} {self.last_name}"
        self.login_attempts = 1

    def describe_user(self):
        """Print a summary of the user’s information."""
        print(
            f"{self.full_name.title()} is {self.age} years old, {self.marital_status}."
        )

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello {self.full_name.title()}, welcome to the party!")

    def increment_login_attempts(self):
        """Increment the value of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login attempts to 0."""
        self.login_attempts = 0


user = User('cillian', 'murphy', 47, 'married')

for i in range(3):
    user.increment_login_attempts()

print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
