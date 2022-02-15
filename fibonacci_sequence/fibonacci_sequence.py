
def fibonacci(n: int) -> int:
    """Generate the Fibonacci sequence to the Nth number"""
    sequence = [0, 1]
    sum = 0
    for i in range(n-2):
        sequence.append(sequence[i] + sequence[i+1])
    return sequence

if __name__ == '__main__':
    num = int(input("Insert fibonacci sequence length: "))
    fibonacci_sequence = fibonacci(num)
    print(fibonacci_sequence)
