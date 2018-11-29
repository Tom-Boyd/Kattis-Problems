import math
def dist(start, end):
    a = abs(float(start[0]) - float(end[0])) ** 2
    b = abs(float(start[1]) - float(end[1])) ** 2
    c = math.sqrt(abs(a - b))
    return c

N = int(input())
coords = []
for i in range(N):
    coords.append(input().split(" "))

tour = list(range(0,N))
used = {i: False for i in range(0, N)}
used[0] = True

print("0")
for i in range(1, N):
    best = -1
    for j in range(0, N):
        if not used[j] and (best == -1 or dist(coords[tour[i-1]], coords[j]) < dist(coords[tour[i-1]], coords[best])):
            best = j
    tour[i] = best
    used[best] = True
    print(best)
