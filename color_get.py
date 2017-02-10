import randomcolor

def get_color(lum):
    rand_color = randomcolor.RandomColor()
    color = str(rand_color.generate(luminosity=lum)[0])
    return color