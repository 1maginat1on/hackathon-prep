def dividers(a):
    counter = 1
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            counter += 1
    return counter


print(dividers(100))