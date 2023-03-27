"""Каждая запись входного файла содержит последовательность символов.
Написать программу, которая определяет, есть ли в этой последовательности
десятичные цифры, и формирует наибольшее число, которое можно составить из
этих цифр. Ведущих нулей в числе быть не должно (за исключением числа 0,
запись которого содержит ровно одну цифру). Если цифр нет, программа должна
вывести в выходной файл сообщение 'NO', а если есть - полученное число"""
with open('input.txt', 'r') as input_file:
    input_data = input_file.read().strip().split('\n')

has_digits = False
max_number = ''

for sequence in input_data:
    digits = []
    for symbol in sequence:
        if symbol.isdigit():
            digits.append(int(symbol))
            has_digits = True
    if digits:
        digits.sort(reverse=True)
        if digits[-1] != 0:
            max_number += ''.join(map(str, digits))

if has_digits:
    if max_number == '':
        max_number = '0'
    with open('output.txt', 'w') as output_file:
        output_file.write(max_number)
else:
    with open('output.txt', 'w') as output_file:
        output_file.write('NO')
