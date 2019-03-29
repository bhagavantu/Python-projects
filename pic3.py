import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#
coffee = Image.open("skyline.jpg")
print(coffee)

print('coffee (RGB)')
plt.imshow(coffee)
plt.show()
r, g, b = coffee.split()

texture = Image.open('texture.jpeg')
print(texture)

print('texture (RGB)')
plt.imshow(texture)
plt.show()

rT, gT, bT = texture.split()

new_image = Image.merge("RGB", (r,g,bT))
plt.imshow(new_image)
plt.xticks([]), plt.yticks([])
plt.show()