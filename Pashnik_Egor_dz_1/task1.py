"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def naive_realisation(duration: int):
    total_time = ''
    print('duration =', duration)
    days = duration // 86400
    hours = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    seconds = duration % 86400 % 3600 % 60
    if duration < 0:
        total_time = 'The time machine has not yet been invented'
    elif duration < 60:
         total_time = f'{seconds} сек'
    elif 60 <= duration < 3600:
        total_time = f'{minutes} мин {seconds} cek'
    elif 3600 <= duration < 86400:
        total_time = f'{hours} час {minutes} мин {seconds} cek'
    else:
        total_time =f'{days} дн {hours} час {minutes} мин {seconds} cek'

    return total_time


def one_cycle_realisation(duration):
    total_time = ''
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    for i in range(duration + 1):
        seconds = duration % 86400 % 3600 % 60
        if i >= 60:
            if i % 60 == 0:
                minutes += 1
                seconds = 0
                if minutes == 60:
                    hours += 1
                    minutes = 0
                    if hours == 24:
                        days += 1
                        hours = 0
            total_time = f'{minutes} мин {seconds} cek'
        else:
            total_time = f'{seconds} сек'
        if i >= 3600:
            total_time = f'{hours} час {minutes} мин {seconds} cek'
        if i >= 86400:
            total_time = f'{days} дн {hours} час {minutes} мин {seconds} cek'
    return total_time


if __name__ == '__main__':
    duration = 25
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))