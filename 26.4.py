import random
s=0
g=0
while g<=2:
    try:
        y= int(random.random()*100)
        h= int(random.random()*100)
        k=y +h
        j=int(input(str(y) +"+" + str(h) + "=" ))
    except ValueError:
         print("Надо числа писать")
         g+=1
         continue
    while j!=k and g<=2:
        try:
            print('не верно')
            g+=1
            if g<=2:
                j=int(input(str(y) +"+" + str(h) + "=" ))
        except ValueError:
            print("Надо числа писать")
            g += 1
    if j==k:
        print('верно')
        s+=1
if g==3:
    print("Игра окончена.Павильных ответов:"+ str(s))
