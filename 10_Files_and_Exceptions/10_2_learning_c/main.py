# 10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. 
# Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, 
# and replace the word Python with the name of another language, such as C. 
# Print each modified line to the screen.


from pathlib import Path


path = Path('/DEV/python_work/10_Files_and_Exceptions/10_2_learning_c/learning_python.txt')
content = path.read_text()

for line in content.splitlines():
    print(line.replace('Python', 'C'))