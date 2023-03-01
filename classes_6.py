# Ну тут без разделения...

class Car(object):
    brand = "Mazda"
    max_speed = 100
    color = 'black'

    def __init__(self, b = brand, ms = max_speed):
        self.brand = b 
        self.max_speed = ms

    def upgrade(self):
        self.max_speed += 25

    @property
    def info(self):
        return [[i for i in self.__dict__],[i for i in self.__dict__.values()]] # Считается за эксперемент? 
    
class Truck(Car):
    brand = "BMW" # не допёр как вытащить из класса car его параметры так что костыль.
    max_speed = '80'
    color = 'white'
    def __init__(self, b = brand, ms = max_speed, chest_count = 1, max_weight = 2000): # Ну тут можно было ещё сделать пометки типа :float :int :str и т.д. но работает и без этого.        
        super().__init__(b, ms)
        self.chest_count = chest_count
        self.max_weight = max_weight


c = Car()
print(c.info)
t = Truck()
print(t.info)

