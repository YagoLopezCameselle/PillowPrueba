from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageDraw, ImageFont
def main():
    image = Image.open("images/image.jpg")

    # crear imagen en blanco
    img = Image.new('RGBA', (800, 400), "blue") 
    img.save('images/blanco.png')
    
    # Invertir colores.
    new_image = ImageChops.invert(image)
    new_image.save("images/image_1.jpg")
    
    # Escala de grises.
    new_image = ImageOps.grayscale(image)
    new_image.save("images/image_2.jpg")
    
    # Resaltar luces.
    new_image = ImageEnhance.Brightness(image).enhance(2)
    new_image.save("images/image_3.jpg")
    
    # Contraste.
    new_image = ImageEnhance.Contrast(image).enhance(4)
    new_image.save("images/image_4.jpg")
    
    # Espejo.
    new_image = ImageOps.mirror(image)
    new_image.save("images/image_5.jpg")
    
    # Cambiar tamaño.
    new_image = image.resize((320, 240))
    new_image.save("images/image_6.jpg")
    
    # Diminuir nitidez.
    new_image = ImageEnhance.Sharpness(image).enhance(-4)
    new_image.save("images/image_7.jpg")
    
    # split la imagen en bandas individuales
    source = image.split()

    R, G, B = 0, 1, 2

    # seleccionamos la region donde el rojo es menos a 100
    mask = source[R].point(lambda i: i < 100 and 255)

    # procesamos la banda verde
    out = source[G].point(lambda i: i * 0.7)

    # pegamos el procesado de la banda de vuelta, pero solo en la zona donde el rojo es menor a < 100
    source[G].paste(out, None, mask)

    # construimos la nueva imagen
    new_image = Image.merge(image.mode, source)
    new_image.save("images/image_8.jpg")

    # invertimos algunos colores manualmente
    r, g, b = image.split()
    new_image = Image.merge("RGB", (b, g, r))
    new_image.save("images/image_9.jpg")

    img = Image.open("images/image.jpg")
    draw = ImageDraw.Draw(img) 
    #font = ImageFont.truetype("/ruta/LiberationSerif-Bold.ttf", 36) 
    draw.text((200, 200),"Titulillo",(0,2,27)) 
    img.save('images/image_11.jpg')

if __name__ == "__main__":
    main()