def listsum(lis):
    # if l == []:
    #     return 0
    # else:
    #     return l[0] + listsum(l[1:])
    return 0 if lis == [] else lis[0] + listsum(lis[1:])


print(listsum([]))  # 0
print(listsum([42]))  # 42
print(listsum([3, 1, 5, 2]))  # 11
