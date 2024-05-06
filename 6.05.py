
import os
def zad1():
    from PIL import Image, ImageEnhance
    n = 'newpapka3'
    os.makedirs(n)
    im = ['card.jpg', 'ncard.jpg', 'pcard.jpg', '8card.jpg']
    for f in im:
        try:
            image = Image.open(f)
            en = ImageEnhance.Contrast(image)
            enimage = en.enhance(2.0)
            enimage.save(f"{n}/enhanced_{f}")
            print(f"Изображение {f} обработано и сохранено как {n}/enhanced_{f}")
        except FileNotFoundError:
            print(f"Файл {f} не найден.")
    print("Все изображения обработаны.")
#zad1()

def zad2():
    from PIL import Image, ImageEnhance
    from pathlib import Path
    n = 'newpapka123'
    d="D:\Pichueva_1-MD-15"
    os.makedirs(n)
    for f in os.listdir(d) :
        g = os.path.join(d, f)
        if os.path.isfile(g) and f.endswith('.jpg'):
            try:
                image = Image.open(f)
                en = ImageEnhance.Contrast(image)
                enimage = en.enhance(2.0)
                enimage.save(f"{n}/enhanced_{f}")
                print(f"Изображение {f} обработано и сохранено как {n}/enhanced_{f}")
            except FileNotFoundError:
                print(f"Файл {f} не найден.")
    print("Все изображения обработаны.")



def zad3():
    d = "D:\Pichueva_1-MD-15"
    for f in os.listdir(d):
        g = os.path.join(d, f)
        if os.path.isfile(g) and f.endswith('.txt'):
            l = open(g,'r').read()
            o = l.read().splitlines()
            for k in o :
                i = open(g,'r')
                i = i.readline()
                print (i.split(","))
#zad3()




