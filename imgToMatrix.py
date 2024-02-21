from PIL import Image
import numpy as np


def RGBToHex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def getHexMatrix(image_path):
    with Image.open(image_path, "r") as image:
        pixels = np.array(image)
        hex_matrix = [list(map(lambda x: RGBToHex(x[0], x[1], x[2]), pixels[i])) for i in range(len(pixels))]
    return hex_matrix

if __name__ == "__main__":
    image_path = "night2.png"
    
    with Image.open(image_path, "r") as image:
        #image = image.convert("h")
        pixels = np.array(image)
        hex_matrix = [list(map(lambda x: RGBToHex(x[0], x[1], x[2]), pixels[i])) for i in range(len(pixels))]
        
    with open('image', 'w') as file:
        file.write(str(hex_matrix))