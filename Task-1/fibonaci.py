def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        c=a+b
        a=b
        b=c
        count =count + 1
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci(n)
