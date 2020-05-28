def log(fn):
    def test(*args, **kwargs):  #после занятия понял что тупанул с условием
        func = fn(*args, **kwargs)
        a = []
        for i in kwargs:
            a.append(str(i)+' = '+str(kwargs[i]))
        b = list(args) + a
        print(fn.__name__, tuple(b), func)
        return func
    return test

@log
def a(x):
    return -x

@log
def b(x, y):
    return x * y

@log
def c(x, y, *args):
    result = x + y
    for arg in args:
        result += arg
    return result

a(1)      # out > a(1) -> -1
b(2, y=3)  # out > b(2, y=3) -> 6
c(1, 2, 3)  # out > c(1, 2, 3) -> 6
