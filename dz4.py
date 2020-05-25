def multiply(fn):
    def test(*args):
        a = 1
        for i in args:
            a *= i
        fn(a)
    return test



@multiply
def func(x):
    print(x)


numbers = map(int, input().split())
func(*numbers)