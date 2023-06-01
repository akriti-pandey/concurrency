import asyncio
import random

async def fibonaccier(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        delay = random.randint(0,1)
        print(f'Waiting for {delay} seconds')
        await asyncio.sleep(delay)  
        fib_1 = await fibonaccier(n - 1)
        fib_2 = await fibonaccier(n - 2)
        return fib_1 + fib_2

async def main():
    userinput = int(input("Enter a positive number: "))
    tasks = [fibonaccier(userinput), fibonaccier(userinput)]  # Create two tasks
    results = await asyncio.gather(*tasks)  # Wait for both tasks to finish
    print(f'Fibonacci number for n={userinput}: {results[0]} and {results[1]}')

asyncio.run(main())
