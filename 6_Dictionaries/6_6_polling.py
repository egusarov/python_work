favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# a list of people who should take the favorite languages poll
people = ['edward', 'phil', 'kira', 'vera']

for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for responding.")
    else:
        print(f"{name.title()}, please take the poll.")
