s = open('input').read().strip().split('\n')
ans = 0
x = 0
works = True
for l in s:
    if l == '':
        print(x)
        if x == 7 and works:
            ans += 1
        x = 0
        works=True
    g = l.split()
    for k in g:
        t,v = k.split(':')
        if not t == 'cid':
            x += 1
        if t == 'byr':
            works = 1920<=int(v)<=2002 and works
        if t == 'iyr':
            works = 2010<=int(v)<=2020 and works
        if t == 'eyr':
            works = 2020<=int(v)<=2030 and works
        if t == 'hgt':
            if v.endswith('cm'):
                works = 150<=int(v[:-2])<=193 and works
            elif v.endswith('in'):
                works = 59<=int(v[:-2])<=76 and works
            else:
                works = False
        if t == 'hcl':
            if len(v)!=7 or v[0]!='#':
                works=False
            else:
                works = all([c.isalnum() for c in v[1:]]) and works
        if t == 'ecl':
            s = 'amb blu brn gry grn hzl oth'
            works= (v in s.split()) and works
        if t=='pid':
            try:
                q = int(v)
                works = len(v)==9 and works
            except:
                works = False
        print(t,v,works)
if x == 7 and works:
    ans += 1
print(ans)