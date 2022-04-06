'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из 
  этого списка, сумма цифр которых делится нацело на 7. 
* Решить задачу под пунктом b, не создавая новый список.)
'''


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_number = 0
    for number in dataset:
        discharge = 10 ** (len(str(number)) - 1)  #для определения разрядности числа
        sum_digit = 0
        number_for_sum = number
        while discharge >= 1:
            sum_digit += number // discharge
            number %= discharge
            discharge /= 10
        if sum_digit % 7 == 0:
            sum_number += number_for_sum
    return sum_number  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
        сумма цифр которых делится нацело на 7"""
    sum_number = 0
    new_list = []

    for i in dataset:
        new_list.append(i + 17)

    for number in new_list:
        discharge = 10 ** (len(str(number)) - 1)  # для определения разрядности числа
        sum_digit = 0
        number_for_sum = number
        while discharge >= 1:
            sum_digit += number // discharge
            number %= discharge
            discharge /= 10
        if sum_digit % 7 == 0:
            sum_number += number_for_sum
    return sum_number  # Верните значение полученной суммы


# решение без создания нового списка
def sum_list_3(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    sum_number = 0
    for number in dataset:
        number += 17
        discharge = 10 ** (len(str(number)) - 1)  # для определения разрядности числа
        sum_digit = 0
        number_for_sum = number
        while discharge >= 1:
            sum_digit += number // discharge
            number %= discharge
            discharge /= 10
        if sum_digit % 7 == 0:
            sum_number += number_for_sum
    return sum_number  # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []

    # сборка списка
    for i in range(1, 1000, 2):
        my_list.append(i ** 3)

    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)
    result_3 = sum_list_3(my_list)
    print(result_3)