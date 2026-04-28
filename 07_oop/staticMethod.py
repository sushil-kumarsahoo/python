class Car:
   def  __init__(self,brand,model):
      self.brand = brand
      self.model = model   
    
   def full_name(self):
      return f"{self.brand} {self.model}"
      
   def fuel_type(self):
      return "petrol or diesel"
   
   @staticmethod
   def general_description():
      return "Cars are means of transport"
      
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model) 
      self.battery_size = battery_size

   def fuel_type(self):
       return "Electric charge"
   
my_car = Car("tata","safari")
print(my_car.general_description())  # object is ignored
print(Car.general_description())  # Static Methods DON'T Need the Object


