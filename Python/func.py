def func(args):
    list1 = []
    for i in args:
        if i > 0:
            list1.append(i)

    return list1


print(func([-2, -1, 0, 1, 2]))

# optional way: (List Comprehension)
input = [1, 2, 3, 4, 5]
newlist = [x for x in input if (x % 2) == 1]
print(newlist)

try:
    print(7/0)
except ZeroDivisionError:
    print('Zero Division')
else:
    print('else')
