import os

def zad1():
    from PIL import Image
    f="tiger-isolated-on-white-background_257123-15084.jpg"
    i=Image.open(f)
    i.show()
    w,h=i.size
    g=i.format
    color=i.mode
    print(f"Размер изображения:ширина{w},Высота{h}")
    print(f'формат изображения{g}')
    print(f"цвет {color}")
zad1()

def zad2():
    from PIL import Image
    f = "1.jpg"
    i = Image.open(f)
    si=i.resize((i.size[0]//3,i.size[1]//3))
    si.save ('smallim.jpg')
    gor=i.transpose(Image.FLIP_LEFT_RIGHT)
    gor.save('gorizim.jpg')
    vert= i.transpose(Image.FLIP_TOP_BOTTOM)
    vert.save('gorizim.jpg')
    mir=i.rotate(180)
    mir.save('mirrorim.jpg')
zad2()

#def zad3():

from PIL import Image, ImageEnhance
n = 'newpapka'
os.makedirs(n)
im = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
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
zad3()

def zad4():
    import os
    i = Image.open("1.jpg")
    draw = ImageDraw.Draw(i)
    font = ImageFont.truetype('arial.ttf', 36)
    textp = (i.size[0] - 200, i.size[1] - 50)
    wm=("что-то")
    draw.text(textp, wm, font=font, fill=(255, 255, 255, 128))
    i.save("1wm.jpg")
zad4()
