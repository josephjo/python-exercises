grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

""" Return sum of list of grades """
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


print "The sum of all the grades is %s." % ("%.2f" % grades_sum(grades))
