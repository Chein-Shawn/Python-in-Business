# A04.py
import math
# read 13 lines (4 integers + 9 probabilities)
lines = [input().strip() for _ in range(13)]

print("LINES:", lines)
print("LEN:", len(lines))

# unpack values
# lines[:4] => Index 0, 1, 2, 3
c, r, N, q = map(int, lines[:4])
p = list(map(float, lines[4:]))

# print("c r N q =", c, r, N, q)
# print("probabilities =", p)

sales = sum(min(q, i)  * p[i] for i in range(len(p)))
profit = math.floor(sales * r - c * q)
print(profit)