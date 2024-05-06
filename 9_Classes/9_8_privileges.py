# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


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


class Admin(User):
    """A simple attempt to model an administrator."""

    def __init__(self, first_name, last_name, age, marital_status):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to admin.
        """
        super().__init__(first_name, last_name, age, marital_status)

        self.actions = Privileges()


class Privileges:
    """List of privileges."""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the administrator’s set of privileges."""
        print("An administrator has the next privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


admin = Admin('cillian', 'murphy', 47, 'married')
admin.actions.show_privileges()
