from collections import Counter
from datetime import datetime


def first():
    a = input('введите числа: ')
    x = input('что ищем: ')
    b = a.split(' ')
    return b.index(x)

def sec():
    a = input('введите числа: ')
    b = a.split(' ')
    c = Counter(b)
    d = iter(c)
    return next(d)

def third():
    a = {}
    while True:
        now = datetime.now()
        timest = datetime.timestamp(now)
        key = input('введите число: ')
        a[key] = timest
        b = iter(a.keys())
        while b:
            try:
                now = datetime.now()
                timest = datetime.timestamp(now)
                i = next(b)
                inptime = a[i]
                test = timest - inptime
                erw = a[i]
                if test > 30:
                    a.pop(i)
                    continue
                else:
                    continue

            except:
                break

        print(a)
    return now

third()
