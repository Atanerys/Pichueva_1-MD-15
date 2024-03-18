def kl(a):
    try:
        a=100/int(a)
    except ValueError:
         print("Надо числа писать")
         continue
         return a

a = input("Введите число ")
d=kl(a)
print(d)
