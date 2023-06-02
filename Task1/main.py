"""
Первая задача:
Задаем длину списка наполненного рандомными числами от 1 до 100.
Вводим искомое число X
Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
"""

import random
len_of_list = int(input('Enter length of list: '))
random_list = [0] * len_of_list
for i in range(len_of_list):
    random_list[i] = random.randint(1, 100)
print(random_list)
target_number = int(input('Enter target number (integer from 1 to 100): '))
sum_of_this_number = 0
for i in range(len_of_list):
    if random_list[i] == target_number:
        sum_of_this_number += 1
if sum_of_this_number > 0:
    print(f'This number is repeated {int(sum_of_this_number)} times in this list.')
else:
    closest_number = 0
    new_closest_number = 0
    difference = 100
    new_difference = 0
    two_closest_numbers = False
    for i in range(len_of_list):
        new_closest_number = random_list[i]
        new_difference = abs(target_number - new_closest_number)
        if new_difference < difference:
            difference = new_difference
            closest_number = new_closest_number
            two_closest_numbers = False
        elif new_difference == difference:
            list_of_closest_numbers = [closest_number, new_closest_number]
            two_closest_numbers = True
    print(f'There is no {int(target_number)} in the generated list. Closest number is {int(closest_number)}.' if two_closest_numbers == False else f'There is no {int(target_number)} in the generated list. Closest numbers are {(list_of_closest_numbers)}.')