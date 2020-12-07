s = open('input')
d = dict()
def dfs(bag):
    global d
    if len(d[bag]) == 0:
        return 0
    ans = 0
    for b in d[bag]:
        ans += dfs(b)
    return len(d[bag]) + ans
for line in s:
    words = line.split()
    bag = words[0]+words[1]
    x = words.index('contain')+1
    curr = ''
    currn = 0
    d[bag] = []
    if 'no' not in line:
        for i in range(x,len(words)):
            if 'bag' in words[i]:
                for _ in range(currn):
                    d[bag].append(curr)
                curr = ''
            else:
                if len(words[i])!=1:
                    curr += words[i]
                else:
                    currn = int(words[i])
print(dfs('shinygold'))
