class Factorial:
    def calculate(self, num):
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

# Main program
number = int(input("Enter a number: "))
factorial_calculator = Factorial()
result = factorial_calculator.calculate(number)
print(f"The factorial of {number} is: {result}")