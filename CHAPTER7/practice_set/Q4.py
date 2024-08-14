number = int(input('Enter the number : '))

for i in range(2, number):
    if (number % i == 0):
        print(i,'Not prime')
    else:
        print(i,'Is prime')
