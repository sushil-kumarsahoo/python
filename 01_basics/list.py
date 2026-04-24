tea_varities = ["Black","green","oolong","white"]

print(tea_varities)

tea_varities[1:2] = ["lemon"]

print(tea_varities)

tea_varities[1:3] = ["green","masala"]
print(tea_varities)

tea_varities[1:1]
print(tea_varities)

tea_varities[1:1] = ["test","test"]
print(tea_varities)

tea_varities[1:3] = []    
print(tea_varities)

for tea in tea_varities:
 print(tea)

 tea_varities.append("Oolong")
 print(tea_varities)

 tea_varities.pop()
 print(tea_varities)

tea_varities.remove("green")
print(tea_varities)

tea_varities.insert(1,"green")
print(tea_varities)

# tea_varities_copy = tea_varities  (safe reference)

# copy of tea_varities
tea_varities_copy = tea_varities.copy()   

tea_varities_copy.append("lemon")
print(tea_varities_copy)

print(tea_varities)

# list comprehension

square_num = [x**2 for x in range(10)]
print(square_num)

