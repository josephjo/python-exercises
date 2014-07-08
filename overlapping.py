""" Function that takes two lists and checks to see if there is a number in common """
def overlapping(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True

    return False


print overlapping([1, 2, 3], [1, 2, 3]) # True
print overlapping([7, 9, 1], [1, 2, 3]) # True
print overlapping([1, 2, 3], [4, 5, 6]) # False
