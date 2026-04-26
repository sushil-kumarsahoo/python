chai_types = {"masala":"spicy","ginger":"Zesty","green":"bitter"}

print(chai_types)

print(chai_types["masala"] )

print(chai_types.get("ginger"))

# chai_types.get("gingery")  //nothing retuns

# chai_types["masalaa"] //it gives error

chai_types["green"] = "fresh"
print(chai_types)

for chai in chai_types: 
 print(chai)
# it gives keys of the chai_types

for chai in chai_types: 
 print(chai,chai_types[chai])          


# it gives all key value pairs
for key, values in chai_types.items():
   print(key, values)

if "masala" in chai_types:
   print("i have masala chai")

print(len(chai_types))

# it adds a new item
chai_types["Earl gray"] = "citrus"
print(chai_types)

# it returns value of "ginger"
chai_types.pop("ginger")

# it removes last item in dictionary
chai_types.popitem() 

# it helps deleting the refrence from memory
del chai_types["green"]
print(chai_types)


chai_types_copy = chai_types.copy()
chai_types_copy["blue tea"] = "flower"
print(chai_types_copy)
print(chai_types)

tea_shop = {
 "chai":{"masala" : "spicy","ginger":"zesty"},
 "tea" : {"green":"mild","black tea":"strong"}
 }

print(tea_shop)

print(tea_shop["chai"])
print(tea_shop["chai"],["ginger"])

squared_nums = {x:x**2 for x in range(6)}
print(squared_nums)

squared_nums.clear()
print(squared_nums)

keys = ["masala","ginger","lemon"]
default_values = "delicious"
new_dict = dict.fromkeys(keys, default_values)
print(new_dict)

