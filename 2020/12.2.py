w = [10,1]
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
        for _ in range(a//90):
            w = [w[1],-1*w[0]]
    if cm == 'F':
        x += w[0]*a
        y += w[1]*a
    if cm == 'L':
        for _ in range(a//90):
            w = [-w[1],w[0]]
    w[0] += ch[0]*a
    w[1] += ch[1]*a
    print(x,y,cm,ch)
print(abs(x)+abs(y))
print(x,y)
    




