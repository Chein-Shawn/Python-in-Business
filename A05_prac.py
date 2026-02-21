# A05.py
import math, re
# read 15 lines (4 integers + 11 probabilities)
lines = input()
lines = lines.replace("'","")
lines = lines.split(" ")
for i in range(4):
    lines[i] = int(lines[i])
c = lines[0]
r = lines[1]
N = lines[2]
s = lines[3]
p = [0] * (len(lines) - 4)
for i in range(4, len(lines)):
    lines[i] = float(lines[i])
    p[i-4] = lines[i]


optimal_order = 0
max_profit = float("-inf")

for order in range(len(p)):
    profit = 0

    for sale in range(len(p)):
        sold = min(order, sale)
        leftover = order - sold
        profit += (r*sold + s*leftover - c*order)*p[sale]
        # if sale == order:
        #     for i in range(sale, len(p)+1):
        #         profit += p[i-1]*order*(r-c)
        # else:
        #     profit += p[sale-1]*(r*sale-s*(order-sale)-c*order)
    if profit > max_profit:
        max_profit = profit
        optimal_order = order

print(optimal_order, math.floor(max_profit))