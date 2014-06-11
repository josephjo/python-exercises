""" Returns the sum of all the digits of a given integer """
def digit_sum(n):
    sum = []
    calc = 0

    for letter in str(n):
        sum.append(letter)

    for num in map(int, sum):
        calc = calc + num

    print "The sum of the digits of %s is %s." % (n, calc)

digit_sum(434)
