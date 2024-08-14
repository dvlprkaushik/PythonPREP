n = int(input('Enter the num : '))

for i in range(1,n+1):
    print(" "*(n-i))
    print("*"*i,end="")
    print("\n")