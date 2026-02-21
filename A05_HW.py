lines = input().replace('"', '').split()
N = int(lines[0])
p = int(lines[1])
d = int(lines[2])
x = [0]*N
y = [0]*N
population = [0]*N
for i in range(N):  
    x[i] = int(lines[3+3*i])
    y[i] = int(lines[4+3*i])
    population[i] = int(lines[5+3*i])

move = [0] * p
coverage_sum = 0
selected = [False] * N
covered = [False] * N
for i in range(p):
    optimal_spot = 0
    optimal_coverage = 0
    for j in range(N):
        if selected[j] == False:
            coverage = 0
            for k in range(N):
                if covered[k] == False and ((x[j]-x[k])**2 + (y[j]-y[k])**2 <= d**2):
                    coverage += population[k]
            if coverage > optimal_coverage:
                optimal_coverage = coverage
                optimal_spot = j
    move[i] = optimal_spot
    selected[optimal_spot] = True
    for k in range(N):
                if covered[k] == False and ((x[optimal_spot]-x[k])**2 + (y[optimal_spot]-y[k])**2 <= d**2):
                    covered[k] = True
coverage_sum = sum(population[k] for k in range(N) if covered[k])   
for i in move:
    print(i+1,end = " ")
print(coverage_sum)
