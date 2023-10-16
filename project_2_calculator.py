calc =True
while calc:
    print("\n1. Enter + for addition")
    print("2. Enter - for subtraction")
    print("3. Enter * for multiplication")
    print("4. Enter / for division")

    num1=float(input("\nEnter a number to perform a operation: "))
    operator=input("Enter a operator: ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print(f"\nAddition of {num1} and {num2} is {num1+num2}")
    elif operator =='-':
        print(f"\nSubtraction of {num2} from {num1} is {num1-num2}")
    elif operator == '*':
        print(f"\nMultiplciation of {num1} and {num2} is {num1*num2}")
    elif operator == '/':
        print(f"\nDivision of {num1} to {num2} is {num1/num2}")
    elif operator == 'off':
        print("\nCalculator is turned off")
        calc = False


