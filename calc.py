from math import sqrt

print("Calculator")
print("Enter Choice")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Cube Root")

choice = int(input("Enter your choice(1,2,3,4,5,6): "))

x = int(input("Enter number"))
if choice == 5:
    print("Square root is", sqrt(x))

elif choice == 6:
    print("Cube root is", x**(1/3) )    

else:
    y = int(input("Enter second number"))

    if choice == 1:
        print("Your answer is: ",x+y)

    elif choice == 2:
        print("Your answer is: ",x-y)

    elif choice == 3:
        print("Your answer is: ",x*y)

    elif choice == 4:
        print("Your answer is: ",x/y)

    else:
        print("Wrong Choice! Try Again")

