def fibonacci_string(n):
    fib_str=['a','b']
    while len(fib_str)<n:
        fib_str.append(fib_str[-1]+fib_str[-2])
    return fib_str[:n]
n=int(input("enter the number of fibonacci string:"))
print(fibonacci_string(n))