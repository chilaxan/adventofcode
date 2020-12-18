
def ev(s):
    ans = -1
    chars = s.split()
    op= -1
    i =  0
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
            if op == -1:
                ans = int(a)
            else:
                ans = eval(str(ans) + op + str(a))
            i = int(j+1)
        elif chars[i].isdigit():
            if op == -1:
                ans = int(chars[i])
            else: 
                ans = eval(str(ans) + op + chars[i])
            i+=1
        else:
            op = str(chars[i])
            i+=1
    return ans
ans = 0
for line in open('input'):
    ans += ev(line)
print(ans)