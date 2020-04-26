def palindrom():
    text = input()
    n = len(text)
    message = 'Является палиндромом'
    for symbol in text:
        if symbol == text[n-1]:
            n -= 1
        else:
            message = 'Не является палиндромом'
            break
    return message


def maximum():
    n = int(input('Введите размерность строки\n'))
    text = input('Введите строку\n')
    text = sorted(list(text[:n:]))
    return text[-1], text[-2]


def nulls():
    text2 = []
    elem = 0
    n = int(input('Введите размерность строки\n'))
    text = input('Введите строку\n')
    text = list(text[:n:])
    while elem < len(text):
        if text[elem] == '0':
            text.remove('0')
            text2.insert(0,0)
        else:
            text2.append(text.pop(elem))
    print(text2)



nulls()
#print(maximum())
#print(palindrom())