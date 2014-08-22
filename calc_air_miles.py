""" Calculate cost per mile for miles needed for a free flight minus any fees """
def calc_air_miles(cost, miles, fees):
    total = (float(cost - fees) / miles) * 100
    total_formatted = "%.2f" % total

    return "You're getting %s cents per mile for a $%s ticket." % (total_formatted, cost)


print calc_air_miles(300, 25000, 20) # 1.12 cpm
print calc_air_miles(16200, 200000, 300) # 7.95 cpm
