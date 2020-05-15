import calendar
import math
import random
from datetime import datetime

def first():
    days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
    d = int(input('день\n'))
    m = int(input('месяц\n'))
    y = int(input('год\n'))
    a = calendar.weekday(y,m,d)
    return days[a]

def sec():
    now = datetime.now()
    m = now.month
    y = now.year
    d = int(input('числовое выражение дня\n'))
    while True:
        a = calendar.weekday(y, m, 1)
        if d == a:
            return y, m
            break
        m -= 1
        if m == 0:
            y -= 1
            m = 12
    return y, m

def third():
    a = int(input('a\n'))
    b = int(input('b\n'))
    c = int(input('c\n'))

    if a+b > c and a+c > b and b+c > a:
        print('существует')
        c1 = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        c2 = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
        c3 = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    else:
        print('не существует')
    return math.degrees(c1), math.degrees(c2), math.degrees(c3)


def fourth():
    a = int(random.randrange(0, 11))
    while True:
        b = int(input('число\n'))
        if a == b:
            print('разгадано')
            break
    return a

print(fourth())

