from user import User


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
