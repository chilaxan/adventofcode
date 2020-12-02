#start
s = open('input').read().strip().split('\n')
ans = 0
for l in s:
    x = l.split()
    a,b = map(int,x[0].split('-'))
    c = x[1][0]
    p = x[-1]
    if p.count(c) >= a and p.count(c)<=b:
        ans += 1
print(ans)

