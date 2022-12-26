class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def getName(self):
        return self.name


a = Animal('Mahesh')
print(a.getname())
