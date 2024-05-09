# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. 
# Store at least three names of cats in the first file and three names of dogs in the second file. 
# Write a program that tries to read these files and print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. 
# Move one of the files to a different location on your system, and make sure the code in the except block executes properly.


from pathlib import Path


files = ['/DEV/python_work/10_Files_and_Exceptions/10_8_cats_and_dogs/dogs.txt',
         '/DEV/python_work/10_Files_and_Exceptions/10_8_cats_and_dogs/cats.txt',
        ]

for file in files:
    print(f"\nReading a file {file}:")
    path = Path(file)
    try:
        content = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        print(content)