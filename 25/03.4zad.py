g1 = ["Иванов", "Пичуева", "Серебрякова", "Федарчук", "Непокульчинская", "Нерсисян", "Удовкин", "Павлова", "Жигалов", "Захаров"]
g2 = ["Алексеев", "Васильев", "Козлов", "Павлов", "Соловьев", "Лебедев", "Максимов", "Егоров", "Дмитриев", "Титов"]
sport = (g1[:5]+ g2[:5])
d = len(sport)
s = tuple(sorted(sport))
student = "Соловьев"
r=""
c=0

for i in sport:
    if student == sport[9] :
        c+=1
        r="да"
if r=="":
    r="net"
print("Группа 1:", g1)
print("Группа 2:", g2)
print("Спортивная команда:", sport)
print("Длина спортивной команды:", d)
print("Отсортированная спортивная команда:", s)
print("Студент", student, "входит в команду:", r)
print("Количество вхождений:", c)