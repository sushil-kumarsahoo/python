def firstfunc(num):
    def actual(x):
        return x ** num
    return actual

f = firstfunc(3)

g = firstfunc(3)

print(f(2))
print(g(3))