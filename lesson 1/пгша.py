import random

Question = []

Task = []

print('вводите вопросы, для окончания записи введите "СТОП"')

while 1:

  data = input()

  if data != 'СТОП':

      Question.append(data)

      print('вопрос записан')

  else:2

      break

print('вводите задания, для окончания записи введите "СТОП"')

while 1:

  data = input()

  if data != 'СТОП':

      Task.append(data)

      print('задание записано')

  else:

      break

print('Вы в игре!')

while 1:

  if input('Правда или действие?:') != 'Действие':

      print(random.choice(Question))

  else:

      print(random.choice(Task))