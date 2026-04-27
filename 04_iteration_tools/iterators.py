nums = [10, 20, 30]

# it = iter(nums)
# it = nums.__iter__()

# print(next(it)) 
# print(next(it))  
# print(next(it)) 

i = iter(nums)
print(i.__next__())
print(i.__next__())
