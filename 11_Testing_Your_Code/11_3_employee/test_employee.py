import pytest
from main import Employee

@pytest.fixture
def employee():
    """Employee that will be available to all test functions."""
    employee = Employee('evgeniy', 'gusarov', 60_000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.annual_salary == 65_000


def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10_000)
    assert employee.annual_salary == 70_000
