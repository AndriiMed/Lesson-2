v = int(input("Введите скорость:"))
t = int(input("Введите время:"))
l = v * t
if v > 0:
    print("В нужном направлении")
if l > 0 & l <= 100:
    print("Отметка", l, "КМ")
else:
    print("Отметка выходит из условий. Измени вводные данные")