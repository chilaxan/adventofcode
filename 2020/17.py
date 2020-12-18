import copy
grid = [[list(s) for s in open('input').read().split('\n')]]
n = len(grid[0])
blank = [list('.'*n) for _ in range(n)] 
def nb(grid,i,j,k):
    ans = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            for z in [-1,0,1]:
                if min(i+x,j+y,k+z)>=0 and not (x==0 and y==0 and z==0):
                    try:
                        if grid[i+x][j+y][k+z] == '#':
                            ans += 1
                    except:
                        pass
    return ans
def show(grid):
    print('SHOW')
    for plane in grid:
        for row in plane:
            print(''.join(row))
        print()

for cycle in range(4):
    print(cycle)
    egrid = [[list('.'*(n+2*cycle+2)) for _ in range(n+2*cycle+2)]]
    for layer in grid:
        l = [list('.'*(n+2*cycle+2))]
        for row in layer:
            l.append(['.'] + row +['.'])
        l.append(list('.'*(n+2*cycle+2)))
        egrid.append(l)
    egrid += [[list('.'*(n+2*cycle+2)) for _ in range(n+2*cycle+2)]]
    grid = copy.deepcopy(egrid)
    newgrid = [[list('.'*(n+2*cycle+2)) for _ in range(n+2*cycle+2)]  for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(len(grid[0][0])):
                # print(nb(grid,i,j,k),i,j,k)
                if grid[i][j][k] == '#':
                    if nb(grid,i,j,k) in [2,3]:
                        newgrid[i][j][k] = '#'
                    else:
                        newgrid[i][k][k] = '.'
                else:
                    if nb(grid,i,j,k) == 3:
                       newgrid[i][j][k] = '#'
    # show(grid)
    grid = copy.deepcopy(newgrid)
    show(grid)
ans = 0
for p in grid:
    for r in p:
        for c in r:
            if c == '#':
                ans += 1
print(ans)

                
