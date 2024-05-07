# 9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.


from random import randint


class Die:
    """Represent a die that can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides the die has."""
        number = randint(1, self.sides)
        print(f"Your lucky number is {number}.")


# Make a 6-sided die and roll it 10 times.
print("\nCreating a 6-sided die ...")
dice_6 = Die()
print("Done")
print("Rollling it 10 times")
for i in range(10):
    dice_6.roll_die()

# Make a 10-sided die and roll it 10 times.
print("\nCreating a 10-sided die ...")
dice_10 = Die(10)
print("Done")
print("Rollling it 10 times")
for i in range(10):
    dice_10.roll_die()

# Make a 20-sided die and roll it 10 times.
print("\nCreating a 20-sided die ...")
dice_20 = Die(20)
print("Done")
print("Rollling it 10 times")
for i in range(10):
    dice_20.roll_die()