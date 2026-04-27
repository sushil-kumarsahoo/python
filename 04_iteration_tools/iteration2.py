f = open('iteration.py')
# f.__next__()
# f.readline()

# print(next(f))
# print(next(f))
# print(next(f))

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())


# A file object is iterable, meaning it works with a for loop

for line in open('iteration.py'):
     print(line, end='')



while True:
       line = f.readline()
       if not line: break
       print(line,end='')