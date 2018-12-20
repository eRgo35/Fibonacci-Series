def fib():  
    
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

def main():
        
    n = input("Podaj ile liczb chesz wygenerowac: ")
    n = int(n)

    for index, fibonacci_number in zip(range(n), fib()):
        print('{i:3}: {f:3}'.format(i=index + 1, f=fibonacci_number))

    input("Press ANY key to terminate...") 

main()

