n = int(input("Введите n: "))
i = 0
n1 = n
while n1 != 0:
    n1 = n1 // 10
    i += 1
sum = n + (10 ** i) * n + n + (100 ** i) * n + (10 ** i) * n + n
print(f"n+nn+nnn = {sum}.")
