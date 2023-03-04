n = int(input())
maxEven = -1
maxOdd = -1
maxRes = -1
q = []

for i in range(8):
    q.append(int(input()))

for j in range(n - 8):
    x = int(input())
    y = q.pop(0)
    q.append(x)
    if y % 2 == 0 and y > maxEven:
        maxEven = y
    elif y % 2 == 1 and y > maxOdd:
        maxOdd = y
    if x % 2 == 0:
        maxRes = max(x * maxOdd, x * maxEven, maxRes)
    elif x % 2 == 1:
        maxRes = max(maxRes, x * maxEven)

print(maxRes)
"""
11
12
45
5
3
17
23
21
20
19
12
26
"""