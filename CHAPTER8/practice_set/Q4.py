def recurr(num):
    if(num==1):
        return 1
    return recurr(num-1)+num
    
    

n = int(input('Enter a number : '))
res = recurr(n)
print(res)