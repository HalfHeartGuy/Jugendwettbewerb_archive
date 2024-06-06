def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next Fibonacci number
        fib_sequence.append(next_number)  # Add the next number to the sequence

    return fib_sequence[:n]  # Return the first n numbers in the Fibonacci sequence

# Test the function
n = 10  # Change this value to calculate the Fibonacci sequence up to a different number
fib_numbers = fibonacci(n)
print(fib_numbers)

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]