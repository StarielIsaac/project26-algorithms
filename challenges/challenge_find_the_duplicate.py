def find_duplicate(nums):
    if not validate_numbers(nums):
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False


def validate_numbers(nums):
    return bool(nums and len(nums) > 1 and
                all(isinstance(num, int) for num in nums) and
                nums[0] >= 0 and len(set(nums)) < len(nums))
