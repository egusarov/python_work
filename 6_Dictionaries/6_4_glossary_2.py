glossary = {
    'python': 'a top programing language',
    'variable': 'a label that you can assign to value',
    'string': 'a series of characters',
    'constant': 'a variable whose value stays the same throughout the life of a program',
    'list': 'a collection of items in a particular order',
    'tuple': 'an immutable list',
    'dictionary': 'a collection of key-value pairs',
    'set': 'a collection in which each item must be unique',
    }

for word, meaning in glossary.items():
    print(f"{word.title()} is {meaning}.")
