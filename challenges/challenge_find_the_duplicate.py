def find_duplicate(nums):
    if not validate_Numbers(nums):
        return False

    if nums[0] in nums[1:]:
        return nums[0]

    return find_duplicate(nums[1:])


def validate_Numbers(nums):
    if not nums or type(nums) == str:
        return False

    if len(nums) == 1 or len(set(nums)) == len(nums):
        return False

    if nums[0] < 0:
        return False

    return True
