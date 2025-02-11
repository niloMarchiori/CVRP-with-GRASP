

class Item():
    def __init__(self,dono=None):
        self.__dono=dono
    @property
    def dono(self):
        return self.__dono


item=Item('Eu')
item.__dono='VC'

print(item.dono)
print(item.__dono)
