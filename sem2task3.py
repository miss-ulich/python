# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.


N = abs(int(input('Введите число N ')))
stop = 0
P = 2
for i in range(N):
    if stop != 1:
        P = P ** i
        if P <= N:
            print(P, end=' ')
            P = 2
        else:
            stop = 1
    else:
        i = N
# n = int(input()) i=0
# while 2 ** i <= n:
#    print(2 ** i)
#    i += 1        