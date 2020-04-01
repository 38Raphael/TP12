def powe(x, n):
    return 1 if n == 0 else x*powe(x, n-1)


print(powe(42, 0))  # 1
print(powe(1, 10))  # 1
print(powe(2, 5))  # 32
print(powe(7, 2))  # 49
