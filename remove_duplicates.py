""" Remove duplicate numbers in a given list and sort in order """
def remove_duplicates(nums):
    duped = []
    for num in nums:
        if num not in duped:
            duped.append(num)

    print sorted(duped)


remove_duplicates([4, 100, 3, 1, 1, 6, 6])
