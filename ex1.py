def modulo(x, y):
    if x - y < 0:
        return x
    else:
        return modulo(x - y, y)


print(modulo(6, 13))  # 6
print(modulo(37, 10))  # 7
print(modulo(8, 2))  # 0
print(modulo(50, 7))  # 1
