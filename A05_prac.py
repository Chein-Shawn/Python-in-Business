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
max_profit = 0
max_sales = 0

for order in range(1, len(p)+1):
    profit = 0
    for sale in range(order+1):
        if sale == order:
            for i in range(sale, len(p)+1):
                profit += 
            profit += p[sale-1]*(r-c)
        else:
            profit += p[sale-1]*(r-c)
        # if sale <= order:
        #     profit += p[sale-1]*(r-c)
        #     max_sales += 1
    profit -= (len(p) - order) * c  # subtract cost of unsold items



# c, r, N = map(int, lines[:3])
# p = list(map(float, lines[3:]))