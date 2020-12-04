def works(pswd):
    return any([pswd[i] == pswd[i+1] and (i+2 >= len(pswd) or pswd[i+1] != pswd[i+2]) and (i-1 < 0 or pswd[i]!=pswd[i-1])for i in range(len(pswd) - 1)]) and all([pswd[i] <= pswd[i+1] for i in range(len(pswd) - 1)])
a = 246515
b = 739105
ans = sum([works(str(p)) for p in range(a,b+1)])
print(ans)
