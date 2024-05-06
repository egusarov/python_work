# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    'odesa': {
        'country':
        'ukraine',
        'population':
        993_120,
        'fact':
        'It\'s known for its beaches and 19th-century architecture, including the Odessa Opera and Ballet Theater.',
    },
    'lviv': {
        'country':
        'ukraine',
        'population':
        721_301,
        'fact':
        'Traces of its Polish and Austro-Hungarian heritage are evident in its architecture, which blends Central and Eastern European styles with those of Italy and Germany.',
    },
    'kyiv': {
        'country':
        'ukraine',
        'population':
        2_884_000,
        'fact':
        'Kyiv is the capital and most populous city of Ukraine. It is in north-central Ukraine along the Dnieper River.',
    },
}

for city, city_info in cities.items():
    print(f"\n{city.title()}")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tInteresting fact: {city_info['fact']}")