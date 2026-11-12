n = int(input())
a = list(map(int, input().split()))
stack = [(0, n - 1)]
while stack:
    lo, hi = stack.pop()
    if lo >= hi:
        continue
    pivot = a[(lo + hi) // 2]
    lt = lo
    i = lo
    gt = hi
    while i <= gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    stack.append((lo, lt - 1))
    stack.append((gt + 1, hi))
print(*a)