""" Print list of even numbers """
def is_even(num):
    even = []
    for n in num:
        if n % 2 == 0:
            even.append(n)

    print even


is_even([1, 2, 3, 4, 5, 6])
