""" For a list of integers, return the product """
def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num

    return "The total is %s." % total


print multiply([10, 2, 1])
print multiply([91, 4, 23, 10, 0, 2, 1, 11])
