i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


def loop(n, step):
    i = 0
    numbers = []

    while i < n:
        numbers.append(i)
        i += step

    return numbers


my_numbers = loop(15, 1)
print(my_numbers)
print(loop(21, 5))
