"""
    Print rating for a Airbnb unit given specific parameters
    Price is the total price of the unit normalized to a score of 1-10
    Location in terms of a score of 1-5
    Amenity in terms of a score of 1-4
    Aesthetics in terms of a score of 1-4
    Other in terms of a score of -1-5
"""
def calculate_score(name, price, location, amenity, aesthetics, other):
    price_rating = 20 - (price * 0.01)
    score = price_rating + location + amenity + aesthetics + other

    print "The price is %s." % price_rating
    print "The location is %s." % location
    print "The amenities are %s." % amenity
    print "The aesthetics are %s." % aesthetics
    print "Other is %s." % other
    print "The rating for \"%s\" is %s.\n\n" % (name, score)


calculate_score("1lDW4R3", 1423, 4, 3, 4, -1)
calculate_score("UNUORK", 1085, 1, 3, 3, -1)
calculate_score("1qu3fhV", 1360, 4, 2, 2, -5)
calculate_score("1iIeuvx", 1183, 4, 2, 3, -3)
calculate_score("1lXn26w", 1369, 5, 4, 2, -1)
calculate_score("1l4aZ7m", 1314, 4, 2, 2, -2)
calculate_score("1pK95Md", 1369, 4, 2, 2, 0)
calculate_score("1uE6AZo", 1292, 4, 1, 3, 2)
calculate_score("1phuJUk", 1140, 1, 3, 2, 0)
calculate_score("1lDW9UB", 1265, 4, 2, 2, 0)
calculate_score("1nirQzV", 1259, 1, 2, 2, -1)
