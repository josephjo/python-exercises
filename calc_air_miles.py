""" Calculate cost per mile for miles needed for a free flight minus any fees """
def calc_air_miles():
    cost = input("Amount you would pay for the flight: $");
    miles = input("Amount of miles it costs: ")
    fees = input("Amount of fees associated with redeeming with miles: $")

    total = (float(cost - fees) / miles) * 100
    total_formatted = "%.2f" % total

    return "You're getting %s cents per mile for a $%s ticket." % (total_formatted, cost)


print calc_air_miles()
