# A04.py
import math
# read 13 lines (4 integers + 9 probabilities)
lines = [input().strip() for _ in range(12)]

print("LINES:", lines)

optimal_order = 0
max_profit = 0

c, r, N = map(int, lines[:3])
p = list(map(float, lines[3:]))

for i in range(len(p)):
    sales = sum(min(i, j)  * p[j] for j in range(len(p)))
    profit = sales * r - c * i
    if profit > max_profit:
        max_profit = math.floor(profit)
        optimal_order = i

# print("c r N q =", c, r, N, q)
# print("probabilities =", p)

print("optimal_order, max_profit: ", optimal_order," ", max_profit)