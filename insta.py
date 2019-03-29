import matplotlib.pyplot as plt 
from PIL import Image
pill = Image.open("pill.jpg")
print(pill)

print('pill (RGB)')
plt.imshow(pill)
plt.show()
r,g,b = pill.split()

texture = Image.open("texture.jpeg")
print(texture)

print('texture (RGB)')
plt.imshow(texture)
plt.show()

rT, gT, bT =texture.split()

new_image = Image.merge("RGB", (r, gT, bT))
plt.imshow(new_image)
plt.xticks([]), plt.yticks([])
plt.show()