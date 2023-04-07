class Vehicle:
    engine_size = 0
    torque = 0
    model = ""
    brand = ""
    cylinder = 0

def show_information(brand: str, model: str, torque: int, cylinder: int, engine_size: int):
    print(f'Brand: {brand}\n'
      f'Model: {model}\n'
      f'Torque: {torque}\n'
      f'Cylinder: {cylinder}\n'
      f'Engine Size: {engine_size}\n')

car_1 = Vehicle() 

car_1.brand = 'Dodge'
car_1.model = 'TRX1500'
car_1.torque = 9000
car_1.cylinder = 5.6
car_1.engine_size = 9

show_information(car_1.brand, car_1.model, car_1.torque, car_1.cylinder, car_1.engine_size)

""" 
print(f'Brand: {car_1.brand}\n'
      f'Model: {car_1.model}\n'
      f'Torque: {car_1.torque}\n'
      f'Cylinder: {car_1.cylinder}\n'
      f'Engine Size: {car_1.engine_size}')
 """

car_2 = Vehicle()

car_2.engine_size = 7.8
car_2.torque = 900
car_2.cylinder = 8.9
car_2.brand = 'Ford'
car_2.model = 'F150'

show_information(car_2.brand, car_2.model, car_2.torque, car_2.cylinder, car_2.engine_size)