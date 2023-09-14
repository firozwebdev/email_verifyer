import time,random

# def fibonacci_iterative(n):
#     fib = [0, 1]
#     for i in range(2, n + 1):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib[n]
#
# # Example usage:
# n = 11 # Change this to the desired Fibonacci number you want to find
# number = fibonacci_iterative(n)

def print_fibonacci_recursive(n, a=0, b=1):
    if n <= 0:
        return
    print(a)
    print_fibonacci_recursive(n - 1, b, a + b)

# Example usage:
n = 10  # Change this to the number of Fibonacci numbers you want to print
print_fibonacci_recursive(100)
# number = range(1,6)
# print(random.choice(number))
# time.sleep(random.choice(number))
# print(f"time delayed is: {time.sleep(random.choice(number))}")

