time_s = int(input("Введите время в секундах: "))
time_m = time_s // 60
time_s = time_s % 60
time_h = time_m // 60
time_m = time_m % 60
if time_h<10:
    print(f"Время: {time_h:02d}:{time_m:02d}:{time_s:02d}")
else:
    print(f"Время: {time_h}:{time_m:02d}:{time_s:02d}")