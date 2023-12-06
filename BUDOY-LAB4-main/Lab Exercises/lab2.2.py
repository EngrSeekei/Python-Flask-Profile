print("This program will tell you if a number is prime or not.")
# Function to check if a number is prime

def is_prime(number):
if number <= 1:
return False
if number <= 3:
return True
if number % 2 == 0 or number % 3 == 0:
return False
i = 5
while i * i <= number:
if number % i == 0 or number % (i + 2) == 0:
return False
i += 6
return True

# Get user input
try:
n = int(input("Enter an integer: "))
if is_prime(n):
print(f"{n} is a prime number.")
else:
print(f"{n} is not a prime number.")
except ValueError:
print("Invalid input. Please enter a valid integer.")