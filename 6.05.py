
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
    import csv
    products = []
    with open('k1.csv', newline='', encoding='utf-8') as csvfile:
        r = csv.reader(csvfile)
        next(r)
        for row in r:
            pname = row[0].strip()
            q = int(row[1].strip())
            price = float(row[2].strip())
            products.append((pname, q, price))
    sum = 0
    print("Нужно купить:")
    for product in products:
        pname, q, price = product
        sum += q * price
        print(f"{pname} - {q} шт. за {price} руб.")
    print(f"Итоговая сумма: {sum} руб.")
#zad3()




