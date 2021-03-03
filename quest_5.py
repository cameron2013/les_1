gain = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издуржек: "))
profit = gain - costs
if profit > 0:
    print(f"Ваша фирма работает с прибылью, равной {profit}.")
    print(f"Рентабельность вашей прибыли равна: {profit / gain}.")
    n = int(input("Сколько сотрудников в Вашей фирме? "))
    print(f"Прибыль в расчете на одного сотрудника равна: {profit / n}.")
elif profit < 0:
    print(f"Ваша фирма работает с убытками, равными {-profit}.")
else:
    print("Ваша фирма на грани убытков.")
