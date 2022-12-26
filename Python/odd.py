# def num():
#     list1 = []
#     for i in range(4, 31, 2):
#         list1.append(i)
#     return list1

# print(num())

# newlist = [a for a in range(4, 31, 2)]
# print(newlist)

input = ["ABC", "", "CDE"]
newlist1 = [a for a in input if len(a) > 0]
print(newlist1)


# def empty(args):
#     list2 = []
#     for i in args:
#         if len(i) > 0:
#             list2.append(i)
#     return list2


# print(empty(["ABC", "", "CDE"]))

letter_count = 0
number_count = 0
special_count = 0
word = '@n1m@l'

for i in word:
    # print(i)
    if i.isalpha():
        letter_count += 1
    elif i.isalnum():
        number_count += 1
    else:
        special_count += 1

print('letter_count --> ', letter_count)
print('number_count --> ', number_count)
print('special_count --> ', special_count)

list3 = [[1, -1, -1],
         [-1, 1, -1],
         [-1, -1, 1]
         ]
sum = 0
for i in list3:
    index1 = list3.index(i)
    for j in i:
        index2 = i.index(j)
        if(index1 == index2):
            print(j)
            sum += j

print(sum)

#
for i in list3:
    index3 = list3.index(i)
    print(list[index3][index3])
