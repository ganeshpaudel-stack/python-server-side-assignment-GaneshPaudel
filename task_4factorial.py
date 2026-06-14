''' Create a python function to calculate factorial of number using recursion'''

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number:"))
print(f"The factorial of {number} is {factorial(number)}")