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

def zad2():
    from PIL import Image
    f = "tiger-isolated-on-white-background_257123-15084.jpg"
    i = Image.open(f)
    si=i.resize(i.size[0]//3,i.size[1]//3))
    si.seve ('smallim.jpg')
    gor=i.transpose(Image.FLIP_Left_RIGHT)
    gor.seve('gorizim.jpg')
    vert= i.transpose(Image.FLIP_TOP_BOTTOM)
    vert.seve('gorizim.jpg')
    mir=i.rotate(180)
    mir.save('mirrorim.jpg')

    def zad3():



