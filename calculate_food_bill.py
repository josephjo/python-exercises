"""
    Calculate tax and tip
    Tip is based on pre-tax amount.
"""
def calc_tax(pretip, tax, tip_percent):
    total = (pretip * (1 + tip_percent / 100.0)) + (pretip * tax / 100.0)
    total = "%.2f" % total

    print "The total for %s%% tip and %s%% tax is $%s." % (tip_percent, tax, total)


calc_tax(34.12, 6, 20)
