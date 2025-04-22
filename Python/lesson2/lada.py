from classes.car import Car
from classes.engine import Engine

car1 = Car()
car1.engine = '123'
car1.model = 'we'
car1.type = '4445'
car2 = Engine()
car2.type_engine = 'qwe'

print(car1.engine, car1.type, car1.model, car2.type_engine, car2.hp)
