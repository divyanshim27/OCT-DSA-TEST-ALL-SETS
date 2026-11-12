def comes_first(x, y):
    if freq[x] != freq[y]:
        return freq[x] < freq[y]
    return x > y

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if comes_first(left[i], right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

n = int(input())
a = list(map(int, input().split()))
freq = {}
for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
unique = list(freq.keys())
unique = merge_sort(unique)
out = []
for x in unique:
    for _ in range(freq[x]):
        out.append(x)
print(*out)