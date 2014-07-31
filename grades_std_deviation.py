grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


class GradesStdDeviation(object):
    """ Get the standard deviation for a list of grades """
    def __init__(self):
        super(GradesStdDeviation, self).__init__()

    """ Return sum of list of grades """
    def grades_sum(self, grades):
        total = 0
        for grade in grades:
            total += grade
        return total

    """ Returns the average of list of grades """
    def grades_average(self, grades):
        sum_of_grades = self.grades_sum(grades)
        average = sum_of_grades / float(len(grades))
        return average

    """ Returns the variance of list of grades """
    def grades_variance(self, grades):
        average = self.grades_average(grades)
        variance = 0

        for grade in grades:
            variance = variance + (average - grade) ** 2
            result = variance / len(grades)
        return result

    """ Returns the standard deviation of list of grades """
    def grades_std_deviation(self, variance):
        variance = self.grades_variance(grades) ** 0.5
        return variance


std = GradesStdDeviation()

print "The sum of all the grades is %s." % ("%.2f" % std.grades_sum(grades))
print "The average of all the grades is %s." % ("%.2f" % std.grades_average(grades))
print "The variance of all the grades is %s." % ("%.2f" % std.grades_variance(grades))
print "The standard deviation of all the grades is %s." % ("%.2f" % std.grades_std_deviation(grades))
