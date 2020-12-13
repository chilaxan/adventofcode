def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - (b // a) * y, y) 
def modinv(a, m): 
    x= extended_euclidean(a, m)[1]
    return x % m 
def crt(m, x): 
    while True: 
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] +  modinv(m[0],m[1]) * x[1] * m[0] 
        temp2 = m[0] * m[1] 
        x.remove(x[0]) 
        x.remove(x[0]) 
        x = [temp1 % temp2] + x  
        m.remove(m[0]) 
        m.remove(m[0]) 
        m = [temp2] + m 
        if len(x) == 1: 
            break
    return x[0] 
s = open('input')
n = int(s.readline().strip())   
buses =  s.readline().strip().split(',')
i = 0
m = []
x = []
for i in range(len(buses)):
    if buses[i]!='x':
        m.append(int(buses[i]))
        x.append(int(buses[i]) - i)
print(crt(m,x))