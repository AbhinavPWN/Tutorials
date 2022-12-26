class Kettle(object):

    def __init__(self, make, price) -> None:
        self.make = make
        self.price = price
        self.on = False


Silmware = Kettle("Silmware", 1200)
print(Silmware.make)
print(Silmware.price)

Balta = Kettle("Balta", 1250)
print("Models: {0.make} =  {0.price} ,{1.make} = {1.price}".format(
    Silmware, Balta))
