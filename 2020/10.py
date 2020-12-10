s = open('input')
lines = list(map(int,s.read().split('\n')))
lines = lines + [0,max(lines)+3]
lines.sort()


# part 1:
x = [0,0,0]
for i in range(len(lines) - 1):
    x[lines[i+1] - lines[i]-1] += 1
print(x[0]*x[-1])

# part 2:
w = []
def ways(lines,i):
    global w
    if w[i] != -1:
        return w[i]
    if i == len(lines) - 1:
        return 1
    ans = 0
    for j in range(i+1,len(lines)):
        if lines[j] - lines[i] < 4:
            ans += ways(lines,j)
    w[i] = ans
    return ans
w = [-1 for _ in range(len(lines))]
print(ways(lines,0))