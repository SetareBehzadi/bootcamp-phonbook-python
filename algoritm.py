def limit(arr, min=None, max=None):
    check_mx = lambda val: True if max is None else (val <= max)
    ckeck_min = lambda val: True if min is None else (val >= min)

    return [val for val in arr if check_mx(val) and ckeck_min(val)]


def top_one(arr):
    test_value = {}
    result = []
    f_result = 0

    for i in arr:
        if i in test_value:
            test_value[i] += 1
        else:
            test_value[i] = 1

    f_result = max(test_value.values())

    for i in test_value.keys():
        if test_value[i] == f_result:
            result.append(i)
        else:
            continue

    return result


from string import ascii_letters


def encrypt(string, key):
    alph = ascii_letters
    result = ""

    for i in string:
        if i not in alph:
            result += i
        else:
            new_key = (alph.index(i) + key) % len(alph)
            result += alph[new_key]

    return result


def dcrypt(string, key):
    key *= -1
    result = encrypt(string, key)
    return result


def search_insert(arr, val):
    high = len(arr) - 1
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        if val <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low


def bead_sort(sequence):
    if any(not isinstance(i, int) or i < 0 for i in sequence):
        raise TypeError('must be posetive integer')

    for _ in range(len(sequence)):
        for j, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            print(j, (rod_upper, rod_lower))
            if rod_upper > rod_lower:
                sequence[j] -= rod_upper - rod_lower
                sequence[j + 1] += rod_upper - rod_lower
            print(f"aaaa {j} : ", sequence)

    return sequence


# print(limit([1,2,3,4,5], 3, None))
print(bead_sort([4, 7, 9, 2, 3, 6, 7]))


class ZigZag:
    def __init__(self, arr1, arr2):
        self.queue = [arr1, arr2]

    def next(self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r

    def has_next(self):
        if self.queue:
            return True
        else:
            return False


z = ZigZag([1, 3, 5, 7], [2, 4, 6, 8])
while z.has_next():
    print(z.next(), end=",")
