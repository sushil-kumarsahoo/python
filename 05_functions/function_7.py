def sum_all(*args):
    # args returns a tuple 
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3,4))