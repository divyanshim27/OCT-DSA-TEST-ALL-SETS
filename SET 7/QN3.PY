n = int(input())
a = list(map(int, input().split()))
lo = 0
hi = n
while lo < hi:
    mid = lo + (hi - lo) // 2
    if a[mid] == 1:
        hi = mid
    else:
        lo = mid + 1
if lo == n:
    print(-1)
else:
    print(lo + 1)