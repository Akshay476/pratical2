def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is prime or not
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
