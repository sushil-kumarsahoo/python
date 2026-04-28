class Car:
   total_car = 0
   def  __init__(self,brand,model):
      self.brand = brand
      self.model = model
    #   self.total_car+=1
      Car.total_car += 1 
    
   def full_name(self):
      return f"{self.brand} {self.model}"
   
   def fuel_type(self):
      return "petrol or diesel"
      
class ElectricCar(Car):
   def __init__(self,brand,model,battery_size):
      super().__init__(brand,model) 
      self.battery_size = battery_size

   def fuel_type(self):
       return "Electric charge"
      

my_tesla = ElectricCar("tesla","model s","85kWh") 
print(my_tesla.fuel_type( ))

safari = Car("tata","safari")
safariThree = Car("tata","nexon")
print(safari.fuel_type())

print(Car.total_car)  # number of objects created

