def div(n):
    for i in range(1,n+1):
        if(n % i == 0):
            lis1.append(i)
    print(lis1)
lis1=[]
n = int(input("enter a number:"))
div(n)
