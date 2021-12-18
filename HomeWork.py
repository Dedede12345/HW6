import sys, random

alphabet = 'А а	Б б	В в	Г г	Д д	Е е \
Ё ё	Ж ж	З з	І і	Й й	К к	Л л	М м \
Н н	О о	П п	Р р	С с	Т т	У у	Ў ў \
Ф ф	Х х	Ц ц	Ч ч	Ш ш	Ы ы	Ь ь	Э э \
Ю ю	Я я'
alphabet = list(alphabet.split())
alphabet = alphabet[::2]

file = open('D:\\HW6.txt', 'w')
for i in range(len(alphabet)):
    file.write(alphabet[i] + '.\n')

print(sys.getsizeof('D:\\HW6.txt'), '- количество байт')

file.close()

file = open('D:\\HW6.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.replace('\n',''), end=' ')
print(f'\n{len(lines)} - количество символов')
file.close()

file = open('D:\\HW6.txt', 'r')
num = [i for i in range(1,10)]
lines = file.readlines()
a = 0
b = []
print(len(lines))
while a <= 10:
    b.append(lines[random.choice(num)])
    a += 1
print(b)


file2 = open('D:\\HW6(1).txt', 'wt')
for i in b:
    file2.write(i.replace('\n', '') + ' ')

file2.close()
file.close()







