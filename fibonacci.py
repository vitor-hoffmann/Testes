num = 13
def fibonacci(num):
    fib = []
    prev, curr = 1, 0
    for i in range(num):
        fib.append(curr)
        prev, curr = curr, curr + prev
        if num in fib:
            return f'{num} pertence'
    return f"{num} nao pertence"

print(fibonacci(num))