""" Prints salary after x number of years for a certain percentage raise """
def calc_raise_years(current_salary, years, raise_percent):
    print "Calculating salary of $%s for %s years with a %s%% raise:\n" \
        % (current_salary, years, raise_percent)

    for x in xrange(1, years + 1):
        current_salary = current_salary * (float(raise_percent) / 100 + 1)
        salary_formatted = "%.2f" % current_salary
        print "Year %s: $%s." % (x, salary_formatted)

    print "---------------------\n "

calc_raise_years(16640, 10, 3)



""" Returns salary after a percentage of raise """
def calc_raise(current_salary, raise_percent):
    new_salary = current_salary * (float(raise_percent) / 100 + 1)
    new_salary_formatted = "%.2f" % new_salary

    return "Calculating salary of $%s with a %s%% raise: $%s." % (current_salary, \
        raise_percent, new_salary_formatted)


print calc_raise(16640, 3)



""" Returns raise percantage given current salary and a desired salary """
def calc_raise_percent(current_salary, desired_salary):
    raise_percent = (float(desired_salary) / float(current_salary) - 1) * 100
    raise_percent_formatted = "%.2f" % raise_percent

    return "Calculating raise percentage for salary from $%s to $%s: %s%%." \
        % (current_salary, desired_salary, raise_percent_formatted)


print calc_raise_percent(16640, 23450)
