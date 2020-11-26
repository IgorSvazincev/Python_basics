#revenue = int(input('Введите значение выручки '))
#costs = int(input('Введите значение издержек '))
revenue = 10000
costs = 4000
if revenue > costs:
    print('Ваша фирма в прибыле - выручка больше издержек')
    profit = revenue - costs
    print(f'Ваша прибыль составляет {profit}')
    profitability = profit / revenue * 100
    print(f'Рентабильность равна {profitability:.2f} %')
    #workers = int(input('Введите численность сотрудников фирмы'))
    workers = 15
    worker_profit = profit / workers
    print(f'Прибыль фирмы в расчёте на одного сотрудника составляет {worker_profit:.2f}')
if revenue < costs:
    print('Вы в убытке - издержки больше прибыли, нужно что-то делать')
if revenue == costs:
    print('Выручка равна издержкам, нужно поднажать')