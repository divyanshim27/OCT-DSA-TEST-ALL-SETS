n, m = map(int, input().split())
pages = list(map(int, input().split()))
if m > n:
    print(-1)
else:
    biggest = 0
    total = 0
    for x in pages:
        total += x
        if x > biggest:
            biggest = x

    def groups_needed(limit):
        groups = 1
        load = 0
        for x in pages:
            if load + x > limit:
                groups += 1
                load = x
            else:
                load += x
        return groups

    lo = biggest
    hi = total
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if groups_needed(mid) <= m:
            hi = mid
        else:
            lo = mid + 1
    print(lo)