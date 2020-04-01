def product(a, b):
    return 0 if b == 0 else a + product(a, b-1)


print(product(5, 2))  # 10
print(product(9, 3))  # 27
