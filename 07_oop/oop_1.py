class Car:
   def  __init__(self,brand,model):
      self.brand = brand
      self.model = model

my_car = Car("toyota","corolla")     
print(my_car.brand)
print(my_car.model)
my_new_car = Car("tata","safari")
print(my_new_car.brand)