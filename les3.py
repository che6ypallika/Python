def my_func(a):
    def help(b):
        return a + b
    return help

test = my_func(3)

print(test(2))

