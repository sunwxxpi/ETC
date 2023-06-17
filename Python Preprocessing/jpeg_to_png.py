import os
from PIL import Image

image_path = './KneeXray/HealthHub Dataset/4/'
image_path2 = './KneeXray/HealthHub Dataset/4_png/'
img_list = os.listdir(image_path)

for i in img_list:
    image = Image.open('{}{}'.format(image_path, i))
    
    ii = i.replace('jpg', 'png')
    
    image.save('{}{}'.format(image_path2, ii))