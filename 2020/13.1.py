s = open('input')
n = int(s.readline().strip())   
buses = [int(x) for x in s.readline().strip().split(',') if x!='x']
i = 0
while True:
    for b in buses:
        if (n+i)%b == 0:
            print(b*i)
            exit()
    i += 1