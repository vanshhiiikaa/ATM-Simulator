num = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: , 5 for modulus: , 6 for exponentiation:   , 7 for floor division: , 8 for square root: , 9 for cube root: , 10 for logarithm:  "))
if num == 1:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a + b)
elif num == 2:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a - b)
elif num == 3:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a * b)
elif num == 4:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a / b)
elif num == 5:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a % b)
elif num == 6:
    a = int(input("Enter the base number: "))
    b = int(input("Enter the exponent number: "))
    print(a ** b)
elif num == 7:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a // b)
elif num == 8:
    import math
    a = int(input("Enter the number: "))
    print(math.sqrt(a))
elif num == 9:
    a = int(input("Enter the number: "))
    print(a ** (1/3))
elif num == 10:
    import math
    a = int(input("Enter the number: "))
    print(math.log10(a))

print("Thank you for using the calculator!")    