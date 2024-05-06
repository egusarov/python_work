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
