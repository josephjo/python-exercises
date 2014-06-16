""" Print list of odd numbers """
def is_odd(num):
    odd = []
    for n in num:
        if n % 2 != 0:
            odd.append(n)

    print odd


is_odd([1, 2, 3, 4, 5, 6])
