def func(*args):
    if len(args) <= 2:
        mul = args[0]
        for i in range(1, len(args)):
            mul = mul * args[i]
        return mul
    else:
        summ = args[0]
        for j in range(1, len(args)):
            summ += args[j]
        return summ


print(func(1, 2, 3, 4))
print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(func(9))
print(func(9, 2))
