class Car:
   def  __init__(self,brand,model):
      self.__brand = brand    # Mangled to _Car__brand
      self.model = model



#    def get_brand(self):
#       return self.__brand + "!"   
   
#    def set_brand(self,value):
#        self.__brand = value
    
# The modern Python way is @property — it gives you controlled access without ugly getters/setters.

   @property                    # Getter
   def brand(self):
     return self.__brand
   
   @brand.setter
   def brand(self, value):     # setter
      self.__brand = value

   def full_name(self):
      return f"{self.__brand} {self.model}"
      
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model) 
      self.battery_size = battery_size


my_tesla = ElectricCar("tesla","model s","85kWh") 

# print(my_tesla.__brand)  # ← NOT truly private, just "mangled"
# What You Write (self.__brand)  ->	What Python Actually Stores (self._Car__brand) if we access like this then it can be accessible


print(my_tesla._Car__brand)

# print(my_tesla.get_brand())
# my_tesla.set_brand("mahindra")
# print(my_tesla.get_brand())  

print(my_tesla.brand)
my_tesla.brand = "mahindra"
print(my_tesla.brand)
