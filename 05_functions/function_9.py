def even_generator(limit):
   for i in range(2,limit+1,2):
      yield i
   
for num in even_generator(10):
   print(num)    

# (yield) is what turns a normal function into a generator.
# Instead of returning one final value and finishing, it:
# gives one value, pauses the function, and remembers where it stopped