def log(fn):
    def test(*args, **kwargs): #может быть больше одной функции? а как если класс? можно ли без вложенной функции?
        func = fn(*args, **kwargs)
        print(fn.__name__, args, kwargs)
        return func #почему тут возврацается значение? как?
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
