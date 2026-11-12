n = int(input())
a = list(map(int, input().split()))
x = int(input())

lo = 0
hi = n - 1
first = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == x:
        first = mid
        hi = mid - 1
    elif a[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1

lo = 0
hi = n - 1
last = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == x:
        last = mid
        lo = mid + 1
    elif a[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1

print(first, last)