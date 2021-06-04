import math

number = int(input("Enter a number: "))

if (math.factorial(number-1) + 1) % number == 0:
    print(f"The number {number} is a prime")
else:
    print(f"The number {number} is not a prime")
