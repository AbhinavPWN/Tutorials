# class Myclass:
#     college = 'Nagarjuna'

#     def __init__(self, name, depart) -> None:
#         print('Constructor')
#         self.name = name
#         self.depart = depart

#     def getname(self):
#         return self.name


# newclass = Myclass('Abhi', 'IT')
# print(newclass.name)
# print(newclass.depart)
# print(newclass.getname())
# print(newclass.college)

class Counter:

    def __init__(self, count):
        self.count = count

    def add(self, val):
        #self.val = val
        self.count += val
        return self.count

    def sub(self, val):
        #self.val = val
        self.count -= val
        return self.count


new1 = Counter(0)
print(new1.add(5))
print(new1.add(6))
print(new1.sub(6))
