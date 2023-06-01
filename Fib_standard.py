def fibonaccier(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_1 = fibonaccier(n - 1)
        fib_2 = fibonaccier(n - 2)
        return fib_1 + fib_2
    
if __name__ == '__main__':     
    userinput = int(input("Enter a positive number: "))
    result = fibonaccier(userinput)
    print(f'Fibonacci number is {result}')

