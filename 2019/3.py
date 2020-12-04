v1=list()
i = [0,0]
f = open('input')
l = f.readline().strip().split(',')
for s in l:
    c = s[0]
    n = int(s[1:])
    h = [0,0]
    if c == 'R':
        h[0]=1
    if c == 'L':
        h[0] = -1
    if c== 'U':
        h[1]=1
    if c == 'D':
        h[1]=-1
    for _ in range(n):
        i[0] += h[0]
        i[1] += h[1]
        v1.append(tuple(i))
i = [0,0]
v2 = list()
l = f.readline().strip().split(',')
for s in l:
    c = s[0]
    n = int(s[1:])
    h = [0,0]
    if c == 'R':
        h[0]=1
    if c == 'L':
        h[0] = -1
    if c== 'U':
        h[1]=1
    if c == 'D':
        h[1]=-1
    for _ in range(n):
        i[0] += h[0]
        i[1] += h[1]
        v2.append(tuple(i))
ix = set(v1).intersection(set(v2))
minm = 1000000
for k in ix:
    minm = min(minm,v1.index(k)+v2.index(k))
print(minm)