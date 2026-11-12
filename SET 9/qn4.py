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
        if left[i][0] <= right[j][0]:
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
intervals = []
for _ in range(n):
    s, e = map(int, input().split())
    intervals.append([s, e])
intervals = merge_sort(intervals)
merged = [intervals[0]]
for i in range(1, n):
    if intervals[i][0] <= merged[-1][1]:
        if intervals[i][1] > merged[-1][1]:
            merged[-1][1] = intervals[i][1]
    else:
        merged.append(intervals[i])
for s, e in merged:
    print(s, e)