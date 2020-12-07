f = open('input').read().split('\n\n')
ans = 0
for group in f:
    lines = group.split('\n')
    s = [0 for _ in range(26)]
    for line in lines:
        for c in line:
            s[ord(c) - ord('a')] +=1
    ans += s.count(len(lines))
print(ans)