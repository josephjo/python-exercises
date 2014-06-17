""" Function to get the median of a list of numbers """
def median(nums):
    nums = sorted(nums)
    middle = len(nums) / 2

    if len(nums) % 2 == 0:
        even_median = float(nums[middle] + nums[middle - 1]) / 2
        print "The median number is %s." % even_median
    else:
        print "The median number is %s." % nums[middle]


median([20, 30, 1, 3, 2, 7, 1])
median([7, 3, 1, 4])
