# Задача 17. 
# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
import random
os.system("cls")

n = random.randint(5, 7)
n = random.randint(3, 7)
spisok = [i for i in range(-n,n+1)]
print('список из N элементов: ', spisok)
print('список из элементов от -N до N:', spisok)

with open('text17.txt', 'w') as positions:
     for i in range(0, int(n/2)):
         positions.write(f'{random.randint(0, len(spisok))}\n') 

multiply=1
with open('text17.txt', 'r') as positions:
    for element in positions:
        print(f'Позиция: {element}', end='')
        multiply = multiply * spisok[int(element.strip())]
print(f'Произведение элементов на этих позициях = {multiply}\n')
