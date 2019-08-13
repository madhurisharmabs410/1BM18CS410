def fibonacci(n):
    n1=0
    n2=1
    for i in range(n):
        print(n1)
        nxt = n1+n2
        n1=n2
        n2=nxt
def main():
    n = int(input("Enter a number"))
    fibonacci(n)
main()
