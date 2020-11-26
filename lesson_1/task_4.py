# number = int(input('Введите целое положительное число: '))
number = int('8745547')
maximum = number % 10
number = number // 10
while number != 0:
    if number % 10 > maximum:
        maximum = number % 10
    number = number // 10
print(maximum)