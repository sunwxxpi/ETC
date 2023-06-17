import cv2
import os

image_path = './KneeXray/test/4/'
image_path2 = './KneeXray/test/4_he/'
img_list = os.listdir(image_path)

for i in img_list:
    img = cv2.imread('{}{}'.format(image_path, i), cv2.IMREAD_GRAYSCALE)
    img2 = cv2.resize(img, dsize=(300, 300), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('{}{}'.format(image_path2, i), img2)