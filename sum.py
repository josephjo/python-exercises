""" Function to add all the numbers in a list """
def sum(list):
    sum = 0
    for num in list:
        sum += num

    return "The sum of the list is %s." % sum


print sum([1, 2, 3])
print sum([23, 1, 3, 0, 42, 99, 2])
