

def zad1():
    from PIL import Image
    img=Image.open('card.JPG')
    img=img.crop((36,50,230,120))
    img.save('ncard.jpg')
    img.show()
zad1()


def zad2():
    from PIL import Image
    c={'День рождения':'card.JPG','8 марта':'8card.JPG','пасха':'pcard.JPG'}
    print(c.keys())
    j=input("введите название праздника для которого нужна открытка?выберите из списка ")
    try:
        cd=c[j]
    except LookupError :
        print("у нас нет такой открытки")
    else:
        h=Image.open(cd)
        h.show()
zad2()


def zad3():
    import sys
    from PIL import Image, ImageDraw,ImageFont
    j=input("кого вы хотите поздравить.Введите имя: ")
    img = Image.open('card.JPG')
    img = img.crop((36, 50, 240, 180))
    txt=ImageDraw.Draw(img)
    f=ImageFont.truetype("arial.ttf",size=20)
    txt.text((70,50),f'{j},поздравляю!',font=f,fill=('#1C0607'))
    img.show()
zad3()



