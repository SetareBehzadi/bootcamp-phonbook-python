class Item:
    def __init__(self, value):
        self.value = value

def min_difference(items):
    total_sum = sum(item.value for item in items)
    dp = [False] * (total_sum + 1)
    dp[0] = True

    for item in items:
        for cur_sum in reversed(range(item.value, total_sum + 1)):
            dp[cur_sum] = dp[cur_sum] or dp[cur_sum - item.value]

    min_diff = float('inf')
    for s1 in range(total_sum + 1):
        if dp[s1]:
            s2 = total_sum - s1
            diff = abs(s1 - 2 * s2)
            min_diff = min(min_diff, diff)

    return min_diff

n = int(input())
projects =[Item(int(input())) for _ in range(n)]
print(min_difference(projects))  # خروجی: 1