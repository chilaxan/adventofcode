def worked(s):
    vis = [False for _ in range(len(s))]
    i = 0
    a=0
    w = True
    while i < len(vis):
        if vis[i]:
            w = False
            break
        vis[i] = True
        n,b = s[i]
        b = int(b)
        if n == 'nop':
            i += 1
        if n == 'acc':
            i += 1
            a += b
        if n == 'jmp':
            i += b
    return w, a
s = [x.split(' ') for x in open('input').read().split('\n')]
for i in range(len(s)):
    t = [x[:] for x in s]
    if s[i][0] == 'nop':
        t[i][0] = 'jmp'
        if worked(list(t))[0]:
            print(worked(t)[1],i)
    elif s[i][0] == 'jmp':
        t[i][0] = 'nop'
        if worked(list(t))[0]:
            print(worked(t)[1],i)