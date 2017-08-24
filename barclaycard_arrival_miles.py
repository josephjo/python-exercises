"""
Calculate optimum Barclaycard Arrival miles so that you're left with exactly
10,000 miles for a second $100 redemption
"""

import locale


def arrival_calculator():
    MINIMUM_REDEMPTION = 10000
    locale.setlocale(locale.LC_ALL, 'en_US')

    balance = input("Current Arrival mile balance: ")

    if balance < MINIMUM_REDEMPTION:
        return "You need a minimum of 10,000 miles to make a redemption."

    redemption = input("Amount of travel redemption: ")

    total = ((MINIMUM_REDEMPTION - (2 * redemption) - balance) / -0.95)
    total_formatted = "%.2f" % total
    total_formatted = locale.format("%d", total, grouping=True)

    return "You should make a redemption of  %s points." % (total_formatted)

print arrival_calculator()
