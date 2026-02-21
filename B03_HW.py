fpath = "/Users/shawn/Desktop/GitHub/Python-in-Business/risk.txt"
with open(fpath, 'r', encoding='utf-8') as file:
    lines = file.readlines()

n, m = map(int, lines[0].split())

    