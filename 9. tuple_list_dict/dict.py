# 1. Создайте пустой словарь с именем captains.

captains = {}

# 2. Используя синтаксис с квадратными скобками, включите следующие
# данные в словарь поочередно:
# • 'Enterprise': 'Picard'
# • 'Voyager': 'Janeway'
# • 'Defiant ': 'Sisko'

captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = ' Sisko'

# 3. Напишите две команды, которые проверяют, существуют ли в словаре
# ключи "Enterprise" и "Discovery". Если ключи не существуют, свяжите
# с ними значения "unknown".

if "Enterprise" in captains:
  print(captains['Enterprise'])
else:
  print('unknown')

if "Discovery" in captains:
  print(captains['Discovery'])
else:
  print('unknown')

# 4. Напишите цикл for для вывода названия корабля и имени капитана,
# содержащихся в словаре. Результат должен выглядеть примерно так:
# The Enterprise is captained Ьу Picard.

for state in captains:
  print(f'The {state} is captained by {captains[state]}')

# 5. Удалите "Discovery" из словаря.

del captains["Enterprise"]

# 6. Дополнителыю: создайте тот же словарь с использованием dict() и пере­
# дайте исходные значения сразу при создании словаря.

captains = {'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant': 'Sisko'}
