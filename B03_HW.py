fpath = "/Users/shawn/Desktop/GitHub/Python-in-Business/risk.txt"
with open(fpath, 'r', encoding='utf-8') as file:
    lines = []
    for line in file:
        lines.append((line.strip()).split())
    print(lines)
        