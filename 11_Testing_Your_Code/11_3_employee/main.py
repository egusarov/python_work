# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5,000 to the
# annual salary by default but also accepts a different raise amount.
# Write a test file for Employee with two test functions, test_give_default
# _raise() and test_give_custom_raise(). Write your tests once without using a
# fixture, and make sure they both pass. Then write a fixture so you don’t have to
# create a new employee instance in each test function. Run the tests again, and
# make sure both tests still pass.


class Employee():
    """A simple try to represent an empolyee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Stores a first name, a last name, and an annual salary of employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Adds $5,000 to the annual salary by default but also accepts a different raise amount."""
        self.annual_salary += raise_amount


# employee = Employee('Evgeniy', 'Gusarov', 60_000)
# print(f"\n{employee.first_name}'s annual salary before raise is ${employee.annual_salary}.")
# print("Salary review is in progress ...")
# employee.give_raise()
# print(f"Annual salary after review is ${employee.annual_salary}.")
