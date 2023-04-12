def prog1():
    from PIL import Image
    Image1 = Image.open('two.jpg')
    croppedIm = Image1.crop((100, 50, 250, 130))
    croppedIm.show()


def prog2():
    from PIL import Image
    a = input("Введите код праздника: (1 - День рождения, 2 - Новый год, 3 - 8 марта, 4 - 23 февраля)")
    one = Image.open("dr.jpg")
    two = Image.open("postcard.jpg")
    three = Image.open("mart.jpg.")
    four = Image.open("23f.jpg.")

    if a == "1":
        one.show()
    elif a == "2":
        two.show()
    elif a == "3":
        three.show()
    elif a == "4":
        four.show()
def prog3():
    from PIL import Image, ImageDraw
    text = input('Передайте поздравление')
    im = Image.new('RGB', (200, 200), color=('#FAACAC'))
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (100, 100),
       text,
        fill=('#1C0606')
    )
    im.show()
prog3()