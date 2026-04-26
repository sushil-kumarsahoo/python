tea_types = ("black","green","oolong")
print(tea_types)

# it gives you error coz it is immutable
tea_types[0] = "lemon"

more_tea = ("herbal","earl grey")
all_tea = more_tea + tea_types
print(all_tea)

if "green" in all_tea:
 print("i have green tea")

more_tea = ("herbal","early grey", "herbal")
more_tea.count("herbal")

(black, green, oolong) = tea_types
print(black)
print(green)


