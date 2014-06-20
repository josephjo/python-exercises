""" Calculate tip """
def calc_food_bill(pretip, percent):
    total = pretip * (1 + percent / 100)

    print "The total for %s%% tip is $%s." % (percent, total)


calc_food_bill(34.12, 20)
