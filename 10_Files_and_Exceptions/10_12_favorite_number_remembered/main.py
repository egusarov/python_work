# 10-12. Favorite Number Remembered: Combine the two programs you wrote in Exercise 10-11 into one file. 
# If the number is already stored, report the favorite number to the user. 
# If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.


from pathlib import Path
import json


path = Path('favorite_number.json')
if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"I know your favorite number! It’s {number}.")
else:
    number = input("Please enter your favorite number: ")
    content = json.dumps(number)
    path.write_text(content)
