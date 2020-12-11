s = open('input')
grid = [list(x) for x in s.read().split('\n')]
def next(grid,i,j,v):
    i += v[0]; j+= v[1]
    while 0<=i<len(grid) and 0<=j < len(grid[0]):
        if grid[i][j] != '.':
            return grid[i][j]
        i += v[0]; j+= v[1]
    return '.'
while True:
    newgrid = [x[:] for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                works = True
                for v in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    if next(grid,i,j,v) == '#':
                        works = False
                if works:
                    newgrid[i][j] = '#'
            if grid[i][j] == '#':
                q = 0
                for v in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    if next(grid,i,j,v) == '#':
                        q += 1
                if q>=5:
                    newgrid[i][j] = 'L'
    if newgrid == grid:
        break
    grid = [x[:] for x in newgrid]
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            ans += 1
print(ans)
