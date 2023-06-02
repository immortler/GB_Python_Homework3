"""
Вторая задача:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо
только английские, либо только русские буквы.

ноутбук
12
"""

word = input(f'Enter any english or russian word in capital letters / '
             f'\nВведите английское или русское слово заглавными буквами: ')
dictionary_of_points = {
    **dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1),
    **dict.fromkeys(['D', 'G'], 2),
    **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
    **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
    **dict.fromkeys(['J', 'X'], 8),
    **dict.fromkeys(['Q', 'Z'], 10),
    **dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1),
    **dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2),
    **dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3),
    **dict.fromkeys(['Й', 'Ы'], 4),
    **dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5),
    **dict.fromkeys(['Ш', 'Э', 'Ю'], 8),
    **dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10),
    **{'K': 5}
}
number_of_points = 0
for i in range(len(word)):
    number_of_points = number_of_points + int(dictionary_of_points.get(word[i]))
print(f'You\'ve got (Вы получаете) {number_of_points} points for your word (очков за слово) {word}.')

