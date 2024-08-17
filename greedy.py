n = int(input())
intervals = []
inputs = list(map(int, input().split()))

for i in range(0, len(inputs), 2):
    l = inputs[i]
    r = inputs[i + 1]
    intervals.append((l, r))

intervals.sort(key=lambda x: x[1])

count = 0
last_end_time = 0

for interval in intervals:
    if interval[0] >= last_end_time:
        count += 1
        last_end_time = interval[1]

print(count)
