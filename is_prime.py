""" Test to see if a given number is prime """
def is_prime(x):
    y = x
    divisor = []

    for y in range(2, x):
        divisor.append(x % y)

    if 0 in divisor or x < 2:
        print x, "is not a prime number."
    else:
        print x, "is a prime number."


is_prime(0) # False
is_prime(2) # True
is_prime(5) # True
is_prime(21) # False
