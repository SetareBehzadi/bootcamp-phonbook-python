def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return "No"

    target = total_sum // 2 # =>11
    check = [False] * (target + 1)
    check[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            check[i] = check[i] or check[i - num]

    return "Yes" if check[target] else "No"

nums = input().split()
num_list = [int(num) for num in nums]

print(canPartition(num_list))
