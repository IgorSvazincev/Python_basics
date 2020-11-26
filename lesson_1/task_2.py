# user_time = int(input('Введите время в секундах: '))
user_time = int('4859')
hour = user_time // 3600
minute = (user_time % 3600) // 60
sec = user_time % 60
print(f'Введёное вами время: {hour:02d}:{minute:02d}:{sec:02d}')
