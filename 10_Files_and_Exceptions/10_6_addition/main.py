# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
# When you try to convert the input to an int, you’ll get a ValueError. 
# Write a program that prompts for two numbers. Add them together and print the result. 
# Catch the ValueError if either input value is not a number, and print a friendly error message. 
# Test your program by entering two numbers and then by entering some text instead of a number.

print("Give me two numbers, and I'll sum them.")
print("Enter 'q' to quit.")

while True:
    try: 
        number_1 = input("\nFirst number: ")
        if number_1 == 'q':
             break
        number_1 = int(number_1)
        
        number_2 = input("Second number: ")
        if number_2 == 'q':
            break     
        number_2 = int(number_2)

    except ValueError:
            print("Input value is not a number. Please try again.")

    else:
        result = number_1 + number_2
        print(f"The sum of two numbers is {result}")