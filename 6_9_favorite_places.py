# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places for
# each person. To make this exercise a bit more interesting, ask some friends to
# name a few of their favorite places. Loop through the dictionary, and print each
# person’s name and their favorite places.

favorite_places = {
    'kira': ['ukraine', 'egypt'],
    'vera': ['bulgaria',],
    'sveta': ['spain', 'israel', 'ukraine'],
    }

for name, countries in favorite_places.items():
    if len(countries) == 1:
        print(f"{name.title()}'s favorite place is:")
    else:
        print(f"{name.title()}'s favorite places are:")

    for country in sorted(countries):
        print(f"\t{country.title()}")
