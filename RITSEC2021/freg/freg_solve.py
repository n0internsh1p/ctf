from PIL import Image, ImageOps

freg = Image.open("freg.png")
pixels = freg.load()

width = 35
height = 51

pix = []
for i in range(height):
    for j in range(width):
        pix += [(pixels[j*4, i*3])]

img = Image.new("RGB", (width, height))
img.putdata(pix)
img = ImageOps.mirror(img).rotate(90, expand=True)
img.save("img.png")