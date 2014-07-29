""" Given two ints, return True if one if them is 10 or if their sum is 10. """
def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True

    return False


print makes10(9, 10) # True
print makes10(9, 9) # False
print makes10(1, 9) # True
