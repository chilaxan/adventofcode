s = open('input')
lines = list(map(int,s.read().split('\n')))
s = set()
x = 22406676
for i in range(2,len(lines)+1):
    for j in range(len(lines)-i):
        
        if sum(lines[j:j+i]) == x:
            print(min(lines[j:j+i])+ max(lines[j:j+i]))

