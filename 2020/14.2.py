s = open('input')
l = []
def bit(mask,val):
    s = bin(val)[2:]
    s = list('0'*(len(mask) - len(s))+s)
    for i in range(len(mask)):
        if mask[i] !='0':
            s[i] = str(mask[i])
    return ''.join(s)
def poss(val):
    global l
    if 'X' not in val:
        l.append(int(''.join(val),2))
        return
    val = list(val)
    for c in range(len(val)):
        if val[c] == 'X':
            val[c] = '0'
            poss(list(val))
            val[c] = '1'
            poss(list(val))
            break

lines = s.read().split('\n')
mem = dict()
mask = ''
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    if line.startswith('mem'):
        l = []
        val = int(line.split()[-1])
        loc = int(line.split()[0][4:-1])
        poss(bit(mask,loc))
        for loca in l:
            mem[loca] = val
ans = 0
for key in mem:
    ans += mem[key]
print(ans)