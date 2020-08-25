
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    setOfNums = set()
    for num1 in nums:
        if num1 in setOfNums:
            return True
        else:
            setOfNums.add(num1)
    return False

    # for num in nums:
    #     if nums.count(num) > 1:
    #         return True
    # return False



nums = [3, 1, 1]

print(containsDuplicate(nums))