# def sumfunc(a, b): return a + b
# print(sumfunc(1, 2))


def multiply(a, b, c):
    return a*b*c


print(multiply(1, 2, 3))


def multi(a, b, c): return a*b*c


print(multi(4, 5, 6))

# a = [1, 2] + [3, 4]
# print(a)

# b = [1, 2, 3, 4]
# w, x, y, z = b
# e, *rest = b
# print(e, rest)

list1 = [1, 2, 3, 4]
print(type(list1))

list2 = 1, 2, 3
print(type(list2))


def ab(*args):
    s = 1
    for i in args:
        s = s * i
    return(s)


print(ab(1, 2, 3))

x = {'m': 1, 'n': 1, 'o': 1}
print(x)

d = dict(x=1, y=2, z=3)
for i in d.items():
    print(i)

# print(d)
print(" ------------------ ")
for i in range(1, 5):
    print(i)
