def works(pswd):
    return any([pswd[i] == pswd[i+1] for i in range(len(pswd) - 1)]) and all([pswd[i] <= pswd[i+1] for i in range(len(pswd) - 1)])
a = 246515
b = 739105
ans = sum([works(str(p)) for p in range(a,b+1)])
print(ans)
