def solution(nums):
    get_N = len(nums) // 2

    nums = set(nums)
    if len(nums) > get_N:
        return get_N
    else:
        return len(nums)