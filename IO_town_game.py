
import io
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('town_game.txt', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s%(levelname)s%(name)s%(message)s')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

town_line = io.StringIO()

town_line.write('Минск')

print(f'Начльное слово: {town_line.getvalue()}')

while True:

    answer = io.StringIO()

    a = town_line.getvalue().replace('ь', '').replace('ъ', "")[-1]

    answer.write(input(f'Введите слово, начинающееся с \'{a.capitalize()}\' '))

    middle = io.StringIO()

    middle.write(answer.getvalue().casefold().replace('ъ', '').replace('ь', ''))

    if answer.getvalue() == 'сдаюсь':
        print(f'Спасибо за игру.\nХод игры: {town_line.getvalue()}')
        # logger.debug(town_line.getvalue())
        town_line.close()
        answer.close()
        break

    if middle.getvalue()[0] == town_line.getvalue()[-1]:
        town_line.write(f' {answer.getvalue()}')
        logger.debug(answer.getvalue())
        middle.close()
        answer.close()
        continue

    elif middle.getvalue()[0] != town_line.getvalue()[-1]:
        print('Попробуйте еще раз или введите \'сдаюсь\'')
        logger.debug(answer.getvalue())
        middle.close()
        answer.close()
        continue

town_line.close()
