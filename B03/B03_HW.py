fpath = "/Users/shawn/Desktop/GitHub/Python-in-Business/risk.txt"
with open(fpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()

n, m = map(int, lines[0].split())
w = [1]*n
paint_colors = []
for i in range(1, m+1):
    start, end, color = map(int, lines[i].split())
    paint_colors.append(color)
    for wall_index in range(start, end+1):
        w[wall_index-1] = color

d = dict()
for i in w:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

results = []
for color in paint_colors:
    count = w.count(color)
    results.append(f'{count} {color}')
print(";".join(results))