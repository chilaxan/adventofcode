s = open('input')
lines = s.read().split('\n')
d = [(1,0),(0,-1),(-1,0),(0,1)]
x = 0
y = 0
p = 0
s = 'ESWN'
for c in lines:
    cm = c[0]
    a = int(c[1:])
    ch = (0,0)
    if cm in s:
        ch = d[(s.index(cm))%4]
    if cm == 'R':
        p += a//90
    if cm == 'F':
        ch = d[p%4]
    if cm == 'L':
        p -= a//90
    x += ch[0]*a
    y += ch[1]*a
    print(x,y,cm,ch)
print(abs(x)+abs(y))
print(x,y)
    




