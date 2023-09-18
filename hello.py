# print('Hello Мир')

# типы данных и переменная
# int, float, boolean, str, list, None
# value = None
# print(type(value))

# a = 123
# b = 1.23
# value = 12334
# # print(a)
# print(b)
# print(value)
# print(type(a))
# print(type(b))
# print(type(value))

# s = 'hello world'
# print(s)
# s = "hello 'world"
# print(s)
# s = 'hello "world'
# print(s)
# s = 'hello \'world'
# print(s)
# s = 'hello \nworld'
# print(s) # вывод строки

# print(a,'-',b,'-',s)
# print('{} - {} - {}'. format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'. format(a, b, s))

# f = True
# print(f)

# list = [] # как массив в c#
# list = [1,2,3]
# list = ['1','2','3','hello',1,2,3, True] # можно, но лучше не хранить в массиве разные типы данных
# print(list)

# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b)

# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a+b)

# Арифметические операции
# +, -, *, /, %, //, **
# **, ⊕, ⊖, *, /, //, %, +, -
# () , Сокращённые операции
# a = 123
# b = 1

# a= 3
# b = 11
# s = 2022
# # print(a, b, s)
# print(a, '-', b, '-',s)
# print(f'{a} - {b} - {s}')
# print('{} - {} - {}'.format(a,b,s))
# # print(f'first - {a} second - {b} third - {s}')

# n = int(input())
# flag = True
# i=2
# while flag:
#     if n % i == 0:# если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# from random import randint
# a = [randint(1, 9) for i in range(int(input('Введите размер массива: ')))]
# print(a)
# print('Встречается', a.count(int(input('Введите искомое число: '))), 'раз')

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count_k = 0
# for i in list_1:
#     if i == k:
#         count_k += 1
# print(count_k)

list_1 = [1, 2, 3, 4, 5, ]
k = 7
# for i in range(len(list_1)):
#     if list_1[i] < k:
#         nearest_num = -k
#     else:
#         nearest_num = nearest_num + 0
#     if list_1[i] >= k and list_1[i] - k <= nearest_num - k:
#         nearest_num = list_1[i]
#     elif list_1[i] <= k and nearest_num - k <= list_1[i] - k:
#         nearest_num = list_1[i]
# print(nearest_num)

# from random import randint
# input_set = [randint(1, 99) for i in range(int(input('Введите размер массива: ')))]
# print(input_set)
# num = int(input('Введите искомое число: '))

input_set = set(list_1)
dif = 0
if k > max(input_set):
    print(max(input_set))
elif k < min(input_set):
    print(min(input_set))
else:
    while True:
        if k - dif in input_set and k + dif in input_set and k - dif != k + dif:
            print(k - dif, k + dif)
            break
        elif k - dif in input_set:
            print(k - dif)
            break
        elif k + dif in input_set:
            print(k + dif)
            break
        else:
            dif += 1