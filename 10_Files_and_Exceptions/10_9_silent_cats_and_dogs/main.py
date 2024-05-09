# 10-9. Silent Cats and Dogs: 
# Modify your except block in Exercise 10-7 to fail silently if either file is missing.


from pathlib import Path


files = ['/DEV/python_work/10_Files_and_Exceptions/10_8_cats_and_dogs/dogs.txt',
         '/DEV/python_work/10_Files_and_Exceptions/10_8_cats_and_dogs/cats.txt',
        ]

file_path = '/DEV/python_work/10_Files_and_Exceptions/10_8_cats_and_dogs/'

for file in files:
    path = Path(file)
    try:
        content = path.read_text()
    except:
        pass
    else:
        print(f"\nReading a file {file.removeprefix(file_path)}:")
        print(content)