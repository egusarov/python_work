# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values
# that are returned.


def city_country(city, country):
    format = f"{city}, {country}"
    return format.title()


a = city_country('odesa', 'ukraine')
print(a)

b = city_country('barcelona', 'spain')
print(b)

c = city_country('milan', 'italy')
print(c)
