class readonly(object):

    def __init__(self, func):
        self.f = func

    def __get__(self, instance, owner):
        return self.f(instance)

    def __set__(self, instance, value):
        raise AttributeError()



class Test(object):
    def __init__(self):
        self.__val = 1

    @readonly
    def val(self):
        return self.__val



test = Test()
print(test.val)  # OK, выводит 1
test.val = 2  # AttributeError

