# 10-1. Learning Python: Open a blank file in your text editor and write a few lines
# summarizing what you’ve learned about Python so far. Start each line with the
# phrase In Python you can. . . . Save the file as learning_python.txt in the same
# directory as your exercises from this chapter. Write a program that reads the file
# and prints what you wrote two times: print the contents once by reading in the
# entire file, and once by storing the lines in a list and then looping over each line.


from pathlib import Path

path = Path('/DEV/python_work/10_Files_and_Exceptions/10_1_learning_python/learning_python.txt')
content = path.read_text()
print("\nPrinting the contents once by reading in the entire file:")
print(content)

print("\nPrinting the contents by storing the lines in a list and then looping over each line:")
for line in content.splitlines():
    print(line)
