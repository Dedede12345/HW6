
from io import StringIO
import random
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Tempreture.log')
file_handler.setLevel(logging.DEBUG)

# file_handler_debug = logging.FileHandler('Tempreture.log')
# file_handler_debug.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s%(name)s%(message)s')

logger.addHandler(file_handler)
# logger.addHandler(file_handler_debug)

file_handler.setFormatter(formatter)
# file_handler_debug.setFormatter(formatter)

temp_list = []

temp_list = [random.randint(0, 255) in range(1024)]

# for i in range(1024):
#     temp = random.randint(0, 255)
#     temp_list.append(temp)

logger.debug(' Temp. list initiated')

with open('Tempreture.bin', 'wb') as f:
    f.write(bytes(temp_list))

logger.info(' Succesfully written')

list = [chr(i) for i in range(32,127)]

print(list)

with open('ident_symbols.txt', 'w', encoding='latin-1') as f:
    for i in list:
        line = f'{i}\n'
        f.write(line)

with open('ident_symbols.txt', 'r', encoding='latin-1') as f:
    f.read()

slav_list = [chr(i) for i in range(1040, 1071)]

slav_dir = dict(zip([i + 1 for i in range(len(slav_list))], slav_list))

print(slav_dir)

kor_word = '사랑'

kor_list = []

for i in kor_word:
    kor_list.append(ord(i))

final_kor_word = f'{hex(kor_list[0])}' + f'{hex(kor_list[1])}'
# print(final_kor_word)

print('\uc0ac''\ub791')


