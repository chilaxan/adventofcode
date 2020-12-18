
def ev(s):
    chars = s.split()
    i =  0
    final = []
    while i < len(chars):
        if '(' in chars[i]:
            x = chars[i].count('(')
            exp = chars[i][1:] + ' '
            j = i+1
            while j < len(chars):
                x += chars[j].count('(')
                x -= chars[j].count(')')
                if x == 0:
                    exp += chars[j][:-1]
                    break
                exp += chars[j] + ' '
                j+=1
            a = ev(exp)
            final.append(str(a))
            i = int(j+1)
        else:
            final.append(chars[i])
            i+=1
    i = 0
    while i < len(final) - 2:
        if final[i+1] == '+':
            final[i] = str(int(final[i]) + int(final[i+2]))
            final.pop(i+1)
            final.pop(i+1)
            i-=1
        i+=1
    return eval(''.join(final))

ans = 0
for line in open('input'):
    print(ev(line))
    ans += ev(line)
print(ans)