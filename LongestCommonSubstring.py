def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # پر کردن جدول dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_str))


def find_longest_common_subsequence(reference, strings):
    max_lcs_length = 0
    longest_lcs = ''
    best_match = ''

    for s in strings:
        lcs_length, lcs_str = lcs(reference, s)
        if lcs_length > max_lcs_length:
            max_lcs_length = lcs_length
            longest_lcs = lcs_str
            best_match = s

    return longest_lcs, max_lcs_length, best_match


reference_string = str(input())
count = int(input())

other_strings = []
for _ in range(count):
    other_strings.append(input())

longest_lcs, lcs_length, best_match = find_longest_common_subsequence(reference_string, other_strings)

print(longest_lcs)
print(lcs_length)
