for a in range(100):
    for b in range(100):
        s = open('input').read().strip().split(',')
        l = list(map(int,s))
        l[1]=int(a)
        l[2]=int(b)
        i = 0
        while l[i]!=99:
            if l[i] == 1:
                l[l[i+3]] = l[l[i+2]]+ l[l[i+1]]
                i+=4
            if l[i] == 2:
                l[l[i+3]] = l[l[i+2]]*l[l[i+1]]
                i+=4
            if l[i]==3:
                
        if l[0]== 19690720:
            print(a,b)

