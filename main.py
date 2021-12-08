print('Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Программа получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

peoples = int(input('Человек в классе: '))

grade_C = 0
grade_B = 0
grade_A = 0

for i in range(peoples):
    grade = int(input('Оценка: '))
    if grade == 3:
        grade_C += 1
    elif grade == 4:
        grade_B += 1
    else:
        grade_A += 1

if (grade_A > grade_B) and (grade_A > grade_C):
    above = 'отличников'
elif (grade_A == grade_B) and (grade_A > grade_C):
    above = 'отличников и хорошистов'
elif (grade_A > grade_B) and (grade_A == grade_C):
    above = 'отличников и троечников'
elif (grade_B > grade_C):
    above = 'хорошистов'
elif (grade_B == grade_C):
    above = 'хорошистов и троечников'
else:
    above = 'троечников'

print('Сегодня больше', above)
