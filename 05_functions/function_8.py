def print_kwargs(**kwargs):
    for key, value in kwargs.items():
# An f-string is a way to insert variables directly inside a string.
        print(f"{key}:{value}")

# **kwargs allows the function to accept any number of keyword arguments
# It stores them in a dictionary
# kwargs = {
#     "name": "shaktiman",
#     "power": "lazer",
#     "enemy": "Dr. jackaal"
# }
# stores like this

print_kwargs(power="lazer",name="sush")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman",power="lazer",enemy="Dr. jackaal")



print_kwargs(age=20, city="Bhubaneswar", skill="coding")
