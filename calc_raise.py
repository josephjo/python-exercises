""" Prints salary after x number of years for a certain percentage raise """
def calc_raise_years(current_salary, years, raise_percent):
    print "Starting salary is $%s.\n" % current_salary
    print "Calculating salary for %s years with a %s%% raise:" % (years, raise_percent)

    for x in xrange(1, years + 1):
        current_salary = current_salary * (float(raise_percent) / 100 + 1)
        salary_formatted = "%.2f" % current_salary
        print "Year %s: $%s." % (x, salary_formatted)


calc_raise_years(16640, 10, 3)



""" Prints salary after a percentage of raise """
def calc_raise(current_salary, raise_percent):
    new_salary = current_salary * (float(raise_percent) / 100 + 1)
    new_salary_formatted = "%.2f" % new_salary

    print "-------------------------------------\n\n "
    return "Calculating salary $%s with a %s%% raise: $%s." % (current_salary, raise_percent, new_salary_formatted)


print calc_raise(16640, 3)
