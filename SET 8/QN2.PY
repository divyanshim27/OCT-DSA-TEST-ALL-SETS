R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(map(int, input().split())))
t = int(input())
lo = 0
hi = R * C - 1
row = -1
col = -1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    value = grid[mid // C][mid % C]
    if value == t:
        row = mid // C
        col = mid % C
        break
    elif value < t:
        lo = mid + 1
    else:
        hi = mid - 1
print(row, col)