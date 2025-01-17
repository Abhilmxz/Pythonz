def fibonacci(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Example usage:
print(fibonacci(6))
print(fibonacci(15)) 
