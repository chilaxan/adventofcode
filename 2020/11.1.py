s = open('input')
grid = [list(x) for x in s.read().split('\n')]
while True:
    newgrid = [x[:] for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                works = True
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]):
                            if grid[x+i][y+j] == '#':
                                works = False
                if works:
                    newgrid[i][j] = '#'
            if grid[i][j] == '#':
                q = 0
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]):
                            if grid[x+i][y+j] == '#':
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
