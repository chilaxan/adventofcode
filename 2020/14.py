s = open('input')
def bit(mask,val):
    s = bin(val)[2:]
    s = list('0'*(len(mask) - len(s))+s)
    for i in range(len(mask)):
        if mask[i] !='X':
            s[i] = str(mask[i])
    return int(''.join(s),2)
lines = s.read().split('\n')
mem = [0 for _ in range(pow(10,6))]
mask = ''
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    if line.startswith('mem'):
        val = int(line.split()[-1])
        loc = int(line.split()[0][4:-1])
        mem[loc] = bit(mask,val)
print(sum(mem))