from PIL import Image,ImageFilter
file="skyline.jpg"
image= Image.open(file)
image.filter(ImageFilter.BLUR).show()
image.filter(ImageFilter.CONTOUR).show()
image= Image.open(file).show()

flower="flowers.jpg"
image= Image.open(flower)
image.filter(ImageFilter.BLUR).show()
image.filter(ImageFilter.CONTOUR).show()
image= Image.open(flower).show()


