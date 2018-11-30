#groupMap will group together all points that can be traversed 
def groupMap(grid):
    h = len(grid)
    w = len(grid[0])
    grouped = [[None for i in range(w)] for j in range(h)]
    currentType = "0"
    currentGroup = 0
    for r in range(h):
        for c in range(w):
            if grouped[r][c] == None:
                currentType = grid[r][c]
                grouped[r][c] = currentGroup
                coordsToDo = [[r,c]]
                while len(coordsToDo) != 0:
                    coord = coordsToDo.pop()
                    r1 = coord[0]
                    c1 = coord[1]
                    if r1 != 0: #look up
                        r2 = r1 - 1
                        if grouped[r2][c1] == None and grid[r2][c1] == currentType:
                            grouped[r2][c1] = currentGroup
                            coordsToDo.append([r2,c1])
                    if r1 != h-1: #look down
                        r2 = r1 + 1
                        if grouped[r2][c1] == None and grid[r2][c1] == currentType:
                            grouped[r2][c1] = currentGroup
                            coordsToDo.append([r2,c1])
                    if c1 != 0: #look left
                        c2 = c1 - 1
                        if grouped[r1][c2] == None and grid[r1][c2] == currentType:
                            grouped[r1][c2] = currentGroup
                            coordsToDo.append([r1,c2])
                    if c1 != w-1: #look right
                        c2 = c1 + 1
                        if grouped[r1][c2] == None and grid[r1][c2] == currentType:
                            grouped[r1][c2] = currentGroup
                            coordsToDo.append([r1,c2])
                currentGroup += 1
    return grouped

#get inputs
r, c = (int(x) for x in input().split(" ",1))
grid = []
for i in range(r):
    grid.append(list(input()))
n = int(input())

grouped = groupMap(grid)

#goes through each query
for i in range(n):
    r1, c1, r2, c2 = (int(x)-1 for x in input().split(" ",3))
    
    #are they in the same group?
    if grouped[r1][c1] == grouped[r2][c2]:
        print("decimal") if grid[r1][c1] == "1" else print("binary")
        continue
    print("neither")
