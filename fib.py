memory = [1, 1]


def fib(n):
    if n < len(memory):
        return memory[n]
    else:
        result = fib(n - 2) + fib(n - 1)
        memory.append(result)
        return result


print(fib(100 - 1))
print(memory)
