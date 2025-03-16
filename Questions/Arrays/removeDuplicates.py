def removeDuplicates(nums):
    if not nums:
        return 0

    n = len(nums)
    idx = 1
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[idx] = nums[i]
            idx += 1
    return nums[:idx]


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(removeDuplicates(nums))