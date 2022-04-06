'''
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    procents = ''

    if 0 < number <= 10 or 20 <= number:
        if number % 10 == 1:
            procents = 'процент'
        elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
            procents = 'процента'
        else:
            procents = 'процентов'
    elif 10 < number < 20:
        procents = 'процентов'

    return f'{number} {procents}'

if __name__ == '__main__':
    for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
        print(transform_string(n))
