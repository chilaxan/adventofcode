s = open('input')
lines = list(map(int,s.read().split('\n')))
s = set()
for i in range(25):
    for j in range(i+1,25):
        s.add(lines[i]+lines[j])
for x in range(26,len(lines)):
    if lines[x] not in s:
        print(lines[x])
        break
    else:
        for i in range(x):
            s.add(lines[x] + lines[i])
