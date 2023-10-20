# Напишите программу, в которой создается следующий список списков:

universities = [
  ['California Institute of Technology', 2175, 37704],
  ['Harvard', 19627, 39849],
  ['Massachusetts Institute of Technology', 10566, 40732],
  ['Princeton', 7802, 37000],
  ['Rice', 5879, 35551],
  ['Stanford', 19535, 40569],
  ['Yale', 11701, 40500]
]

# Определите функцию enrollment_stats (),получающую один параметр. Этим
# параметром должен быть список списков, в котором каждый вложенный список содержит три элемента:
# 1) название университета;
# 2) общее количество зачисленных студентов;
# 3) ежегодная плата за обучение.
# Функция enrollment_stats() должна возвращать два списка. Первый содер­
# жит все данные о зачисленных зарегистрированных студентах, а второй - все
# данные о плате за обучение.
# Затем определите две функции -
# mean() и median( ), которые получают один
# списковый аргумент и возвращают среднее значение и медиану по каждому списку соответственно.
# Используя universities, enrollment_stats(), mean() и median(), вычислите
# общее количество студентов, общую плату за обучение, среднее и медианное
# количество студентов, а также среднюю и медианную плату за обучение.
# Наконец, выведите все значения и отформатируйте вывод, чтобы он выглядел так:
# ******************************
# Total students: 77,285
# Total tuition: $ 271,905
# Student mean: 11,040.71
# Student median: 10,566
# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
# ******************************

def enrollment_stats(list_of_university):
    total_student = []
    total_tuition = []
    for university in list_of_university:
      total_student.append(university[1])
      total_tuition.append(university[2])
    return total_student, total_tuition
    
def mean(values):
   return sum(values) / len(values)

def median(values):
   values.sort()
   if len(values) % 2 == 1:
      center_index = int(len(values) / 2)
      return values[center_index]
   else:
      left_center_index = (len(values) - 1) // 2
      right_center_index = (len(values) + 1) // 2
      return mean([values[left_center_index], values[right_center_index]])


totals = enrollment_stats(universities)
print(f'Total students: {sum(totals[0]):,}')
print(f'Total tuition: $ {sum(totals[1]):,}')
print(f'Student mean: {mean(totals[0]):,.2f}')
print(f'Student median: {median(totals[0]):,}')
print(f'Tuition mean: {mean(totals[1]):,.2f}')
print(f'Tuition median: {median(totals[1]):,}')
