# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначное число :')
a = (input())
a = int(a)
d1 = a % 10
d2 = a % 100 // 10
d3 = a // 100
print("Сумма цифр трехзначного числа :",d1 + d2 + d3)
