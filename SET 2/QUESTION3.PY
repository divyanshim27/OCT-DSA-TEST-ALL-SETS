n, T = map(int, input().split())
a = list(map(int, input().split()))
best = 0
current = 0
for x in a:
    if x >= T:
        current += 1
        if current > best:
            best = current
    else:
        current = 0
print(best)