"""Каждая запись входного файла содержит последовательность символов.
Написать программу, которая определяет, есть ли в этой последовательности
десятичные цифры, и формирует наибольшее число, которое можно составить из
этих цифр. Ведущих нулей в числе быть не должно. Если цифр нет, программа должна
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
        max_number += ''.join(map(str, digits))

if has_digits:
    with open('output.txt', 'w') as output_file:
        if max_number=='0'*len(max_number):
            output_file.write('0')
        else:
            output_file.write(max_number)
else:
    with open('output.txt', 'w') as output_file:
        output_file.write('NO')
