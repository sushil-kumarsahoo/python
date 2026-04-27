x = 99

def func():
    # global x   // avoid this
    x = 12

func()
print(x)    