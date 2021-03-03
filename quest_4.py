a = int(input("Введите число: "))
b = 0
while a != 0:
    if (a % 10) > b:
        b = a % 10
    a = a // 10
print(f"Наибольшая цифра в числе: {b}")
