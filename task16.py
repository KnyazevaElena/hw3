# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих cтроках записаны N целых чисел Ai.
# Последняя строка содержит число X
# Пример: n = 5; элементы 1 2 3 4 5; x = 3; 


N = int(input('Введите размер элементов в массиве: '))
list_n = input('Введите элементы списка через пробел: ').split()
mass = list(map(int, list_n))
x = int (input('Введите число х: '))
count = 0
for i in range(N):
    if mass[i] == x:
        count += 1
print(f'Число {x} встречается  {count} раз.')