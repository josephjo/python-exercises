grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

""" Return sum of list of grades """
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

""" Returns the average of list of grades """
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

""" Returns the variance of list of grades """
def grades_variance(grades):
    average = grades_average(grades)
    variance = 0

    for grade in grades:
        variance = variance + (average - grade) ** 2
        result = variance / len(grades)
    return result


print "The sum of all the grades is %s." % ("%.2f" % grades_sum(grades))
print "The average of all the grades is %s." % ("%.2f" % grades_average(grades))
print "The variance of all the grades is %s." % ("%.2f" % grades_variance(grades))
