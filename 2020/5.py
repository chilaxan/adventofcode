s = open('input')
maxm = 0
def solve(line):
    row = int(line[:7].replace('B','1').replace('F','0'),2)
    col = int(line[7:10].replace('R','1').replace('L','0'),2)
    return 8*row+col
ids = []
for line in s:
    ids.append(solve(line))
for n in range(1,1000):
    if n-1 in ids and n+1 in ids and not (n in ids):
        print(n)