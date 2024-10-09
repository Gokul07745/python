def armstrong(num):
    strring= str(num)
    sum=0
    for i in strring:
        sum+=int(i)**len(strring)
    return True if sum==num else False
print(armstrong(153))