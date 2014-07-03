""" Given two numbers, figure out which is greater """
def max_num(num1, num2):
    if num1 == num2:
        return "The two numbers are equal!"
    elif num1 > num2:
        return "%s is the greater number." % num1
    else:
        return "%s is the greater number." % num2


print max_num(2, 3)
print max_num(0, 99)
print max_num(1, 1)



""" Given three numbers, figure out which is greater """
def max_num_three(num1, num2, num3):
    if num1 == num2 == num3:
        return "The three numbers are equal!"
    elif num1 > num2 and num1 > num3:
        return "%s is the greater number." % num1
    elif num2 > num1 and num2 > num3:
        return "%s is the greater number." % num2
    else:
        return "%s is the greater number." % num3

print max_num_three(1, 1, 1)
print max_num_three(3, 1, 1)
print max_num_three(21, 90, 11)
print max_num_three(1, 2, 6)
