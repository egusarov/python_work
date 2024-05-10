# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. 
# Use json.dumps() to store this number in a file. 
# Write a separate program that reads in this value and prints the message “I know your favorite number! It’s _____.”


from pathlib import Path
import json


number = input("Please enter your favorite number: ")

path = Path('favorite_number.json')
content = json.dumps(number)
path.write_text(content)