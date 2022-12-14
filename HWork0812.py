n = int(input('Введите колличество учеников : '))
k = int(input('Введите колличество яблок : '))
in_arms = n // k
in_box = n % k
print(f'У школьников по {in_arms} яблок')
print(f'В корзине {in_box} яблок')

class_1 = int(input('Введите колличество учеников класса А : '))
class_2 = int(input('Введите колличество учеников класса Б : '))
class_3 = int(input('Введите колличество учеников класса В : '))
all_pupil = class_1 + class_2 + class_3
number_desks = int(all_pupil / 2)
ost_pupil=int(all_pupil%2)
all_desks=number_desks + ost_pupil
print(f'Нужно {all_desks}  парт')


number=int(input('Введите трехзначное число: '))
units=int(number%10)
tens=int(number//10%10)
hundreds=int(number//100)
print(f'{units}{tens}{hundreds}')