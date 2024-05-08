# 10-5. Guest Book: Write a while loop that prompts users for their name. 
# Collect all the names that are entered, and then write these names to a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.


from pathlib import Path


path = Path('guest_book.txt')

prompt = "\nPlease enter your name:"
prompt += "\n(enter 'stop' if finish) "

names = []
while True:
    name = input(prompt)
    if name == 'stop':
        break
    else:
        names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in names:
    file_string += f"{name}\n"

path.write_text(file_string)