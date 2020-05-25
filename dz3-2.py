import numpy
from functools import reduce
massiv = [7, 4, 2, 5, 1]

def sum(a,b):
    return a + b

def multiply(a, b): #надо не делать с нуля как-то
    return a * b

def join(a,b):
    return a * 10 + b

def unite(): # передаю сет
    ...

def reverse(): # передаю лист или деку и добавляю в нудевое значение a: list
    ...

def negated(a):
    return a * -1

def inverted(a):
    return 1/a

def squared(a):
    return a * a
#
def odds(a):
    return a %

def evens(a):
    return not a % 2 == 0

def primes(a): #хз
    x = range(1,a+1)
    counts = 0
    for i in x:
        if a % i == 0:
            counts += 1
    if counts == 2:
        return a





# n = int(input('введите число\n'))
# lst = numpy.random.randint(0, 10, n)
# command_list = {'sum':sum, 'multiply':multiply, 'join':join, 'unite':unite, 'reverse':reverse, 'negated':negated, 'inverted':inverted, 'squared':squared, 'odds':odds, 'evens':evens, 'primes':primes}
# command = input('введите команды').split()

# re = list(map(command_list[command[1]], massiv))
# re2 = list(filter(command_list[command[2]], re))
# re3 = reduce(command_list[command[0]], re2, 0)
re3 = list(filter(evens, massiv))
print(re3)