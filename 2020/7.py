s = open('input')
d = dict()
e = dict()
def dfs(word):  
    global d,e
    e[word]=True
    if word not in d:
        return
    for x in d[word]:
        if not e[x]:
            dfs(x)
    
for line in s:
    words = line.split()
    bag = words[0]+words[1]
    x = words.index('contain')+1
    curr = ''
    e[bag]=False
    if 'no' not in line:
        for i in range(x,len(words)):
            if 'bag' in words[i]:
                if curr not in d:
                    d[curr] = [bag]
                else:
                    d[curr].append(bag)
                curr = ''
                e[curr]=False
            else:
                if len(words[i])!=1:
                    curr += words[i]
dfs('shinygold')
ans = 0
for key in e:
    if e[key]:
        ans += 1
print(ans)
