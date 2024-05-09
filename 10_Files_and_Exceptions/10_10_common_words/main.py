# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org ) and find a few texts you’d like to analyze. 
# Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase appears in a string. 
# For example, the following code counts the number of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, 
# regardless of how it’s formatted.
# Write a program that reads the files you found at Project Gutenberg and 
# determines how many times the word 'the' appears in each text. 
# This will be an approximation because it will also count words such as 'then' and 'there'. 
# Try counting 'the ', with a space in the string, and see how much lower your count is.


from pathlib import Path


books = ['/DEV/python_work/10_Files_and_Exceptions/10_10_common_words/Moby-Dick.txt',
         '/DEV/python_work/10_Files_and_Exceptions/10_10_common_words/Tarzan of the Apes.txt',
        ]
file_path = '/DEV/python_work/10_Files_and_Exceptions/10_10_common_words/'

for book in books:
    path = Path(book)
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        print(f"\nReading a book {book.removeprefix(file_path)} ...")
        print("Determining how many times the word 'the' appears in the text ...")

        res = content.lower().count('the ')
        print(f"The word 'the' appears in the text {res} times.")