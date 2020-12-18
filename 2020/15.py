s = open('input')
l= [2,20,0,4,1,17]
visited = dict()
for i in range(len(l)-1):
    visited[l[i]] = i
while len(l) < 30000000:
    if l[-1] not in visited:
        l.append(0)
    else:
        l.append(len(l) - 1 - visited[l[-1]])
    visited[l[-2]] = len(l)-2
    if len(l)%10000 == 0: print(len(l))
print(l[-1])