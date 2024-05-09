# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, 
# even if they make a mistake and enter text instead of a number.


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