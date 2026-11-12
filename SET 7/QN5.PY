n = int(input())
a = list(map(int, input().split()))
h = int(input())

lo = 0
hi = n - 1
while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] < a[mid + 1]:
        lo = mid + 1
    else:
        hi = mid
peak = lo

ans = -1
lo = 0
hi = peak
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == h:
        ans = mid
        break
    elif a[mid] < h:
        lo = mid + 1
    else:
        hi = mid - 1

if ans == -1:
    lo = peak + 1
    hi = n - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == h:
            ans = mid
            break
        elif a[mid] > h:
            lo = mid + 1
        else:
            hi = mid - 1

print(ans)