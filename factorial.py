""" Returns the factorial of a given integer """
def factorial(x):
    factorial = 1
    y = x

    while x > 0:
        factorial = x * factorial
        x = x - 1

    print "The factorial of %s is %s." % (y, factorial)


factorial(4)
