import numpy
from functools import reduce
massiv = [5, 8, 6, 2, 9]

def sum(a,b):
    return a + b

def multiply(a, b): #надо не делать с нуля как-то
    return a * b

def join(a,b):
    return a*10+b

# def unite():
# def reverse():

def negated(a):
    return a * -1

def inverted(a):
    return 1/a

def squared(a):
    return a * a
#
def odds(a):
    return a % 2

def evens(a):
    return not a % 2

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
command_list = {'join':join, 'negated':negated, 'primes':primes}
command = input('введите команды').split()

# re = list(map(command_list[command[1]], massiv))
# re2 = list(filter(command_list[command[2]], re))
re3 = reduce(command_list[command[0]], massiv,0)

print(re3)