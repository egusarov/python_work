rivers = {
    'nile': 'egypt',
    'dnipro': 'ukraine',
    'amazonas': 'south аmerica'
    }

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()
# Use a loop to print the name of each river included in the dictionary.
for river in rivers.keys():
    print(river.title())
print()
# Use a loop to print the name of each country included in the dictionary.
for country in rivers.values():
    print(country.title())