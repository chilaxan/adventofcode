s = open('input').read().split('\n\n')
p1 = s[0].split('\n')
r = [0 for _ in range(1000)]
ranges = []
for line in p1:
    name = line.split(':')[0]
    line = line.split(': ')[-1].split(' or ')
    r1,r2 = line
    x,y = map(int,r1.split('-'))
    for i in range(x,y+1):
        r[i] = True
    x2,y2 = map(int,r2.split('-'))
    for i in range(x2,y2+1):
        r[i] = True
    ranges.append((name,(x,y),(x2,y2)))
tickets = [list(map(int,line.split(','))) for line in s[2].split('\n')[1:]]
tick = []
for i in range(len(tickets)):
    ticket = tickets[i]
    works = True
    for j in ticket:
        if not r[j]:
            works = False
            break
    if works:
        tick.append(tickets[i])
t = [set(ranges) for _ in range(len(ranges))]
for x in tick:
    for j in range(len(ranges)):
        work = set()
        for i in range(len(ranges)):
            if ranges[i][1][0] <= x[j] <= ranges[i][1][1]:
                work.add(ranges[i])
            elif ranges[i][2][0] <= x[j] <= ranges[i][2][1]:
                work.add(ranges[i])
        t[j] = work.intersection(t[j])
used = set()
for _ in range(1000):
    for i in range(len(t)):
        if len(t[i]) == 1:
            used.add(list(t[i])[0])
        else:
            t[i] = t[i].difference(used)

my = list(map(int,s[1].split('\n')[-1].split(',')))
mult = 1
for i in range(len(t)):
    if list(t[i])[0][0].startswith('departure'):
        mult*=my[i]
print(mult)
