def s(a,b):
    s = open('input').read().strip().split('\n')
    for i in range(len(s)):
        s[i] = s[i]*1000
    x,y=0,0
    ans = 0
    while x < len(s[0]) and y < len(s):
        if s[y][x] == '#':
            ans += 1
        x += a
        y += b
    return ans
print(s(1,1)*s(3,1)*s(5,1)*s(7,1)*s(1,2))