s='да'
while s=='да':
import random
guesses_made = 0
name = input('Привет! Как тебя зовут?\n')
number = random.randint(1, 30)
print('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))
while guesses_made < 6:
    guess = int(input('Введи число: '))
    guesses_made += 1

    if guess < number:
        print('Твое число меньше того, что я загадал.')

    if guess > number:
        print('Твое число больше загаданного мной.')

    if guess == number:
        break

if guess == number:
    print('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
else:
    print('А вот и не угадал! Я загадал число {0}'.format(number))
s=input('Если хотите сыграть снова введите да: ')