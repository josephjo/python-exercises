""" Prints the entire "99 Bottles of Beer" song """
def bottles_of_beer():
    for x in reversed(xrange(1,100)):
        print ("%s bottles of beer on the wall, %s bottles of beer.\n" \
               "Take one down, pass it around, %s bottles of beer on the wall.\n") \
                % (x, x, x-1)


bottles_of_beer()
