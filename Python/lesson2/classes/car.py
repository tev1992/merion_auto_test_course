from engine import Engine

class Car:
    model = ''
    type = ''
    vol = ''
    engine = None


car1 = Car()
car1.engine = Engine()
car1.engine.type_engine = 'KJKJKJ'
car1.model = 'YA'

print(car1.engine.type_engine + car1.model)
