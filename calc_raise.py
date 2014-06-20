""" Prints salary after x number of years for a certain percentage raise """
def calc_raise(current_salary, years, raise_percent):
    print "Starting salary is $%s.\n" % current_salary
    print "Calculating salary for %s years with a %s%% raise:" % (years, raise_percent)

    for x in xrange(1, years + 1):
        current_salary = current_salary * (raise_percent / 100 + 1)
        current_salary_shortened = "%.2f" % current_salary

        print "Year %s: $%s." % (x, current_salary_shortened)


calc_raise(63103, 12, 2.1)
