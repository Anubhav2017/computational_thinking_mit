def fib(n):
    if(n==1 or n==0):
        return 1
    else:
        return fib(n-1)+fib(n-2)

if __name__=="__main__":
    print(fib(40))
