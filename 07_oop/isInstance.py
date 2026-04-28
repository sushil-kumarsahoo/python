class Car:
   def  __init__(self,brand,model):
      self.__brand = brand
      self.__model = model   

   def get_brand(self):
      return self.__brand + "!"  

   def full_name(self):
      return f"{self.__brand} {self.__model}"
      
   def fuel_type(self):
      return "petrol or diesel"
   
   @staticmethod
   def general_description():
      return "Cars are means of transport"
   @property
   def model(self):
      return self.__model
      
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model) 
      self.battery_size = battery_size

   def fuel_type(self):
       return "Electric charge"
   
# my_tesla = ElectricCar("tesla","model s","85kWh")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

# my_tata = Car("tata","nexon")
# print(isinstance(my_tata,ElectricCar))
# print(isinstance(my_tata,Car))


class Battery:
   def battery_info(self):
      return "this is battery"

class Engine:
   def engine_Info(self):
      return "this is engine"

class ElectricCar2(Battery,Engine,Car):
   pass

my_newTesla = ElectricCar2("Tesla","model s")
print(my_newTesla.engine_Info())
print(my_newTesla.battery_info())
