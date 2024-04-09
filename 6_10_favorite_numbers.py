# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {
    'kira': [1, 7,],
    'vera': [3, 5, 9,],
    'sveta': [5,],
    'jeka': [8, 9, 15,],
    'eva': [13,],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favorite number is {numbers}.")
    else:
        print(f"{name.title()}'s favorite numbers are: {numbers}.")
