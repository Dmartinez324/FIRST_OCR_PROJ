import cv2
from PIL import Image

img_file = "data/img1.jpg"

im = Image.open(img_file)

im.save("temp/preImg1.jpg")



