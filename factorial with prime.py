class Factorial:
    def calculate(self, num):
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

# Main program
number = int(input("Enter a number: "))
factorial_calculator = Factorial()

# Calculate factorial
factorial_result = factorial_calculator.calculate(number)
print(f"The factorial of {number} is: {factorial_result}")

# Check if the number is prime
if factorial_calculator.is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")