import cv2
import os

image_path = './KneeXray/test/0/'
image_path2 = './KneeXray/test_flip/0/'
img_list = os.listdir(image_path)
img_list_left = [file for file in img_list if file.endswith("L.png")]
img_list_right = [file for file in img_list if file.endswith("R.png")]

for i in img_list_left:
    img = cv2.imread('{}{}'.format(image_path, i), cv2.IMREAD_GRAYSCALE)
    
    img_flip = cv2.flip(img, 1) # 0 : Vertical Flip, 1 : Horizontal Flip

    cv2.imwrite('{}{}'.format(image_path2, i), img_flip)

for i in img_list_right:
    img = cv2.imread('{}{}'.format(image_path, i), cv2.IMREAD_GRAYSCALE)
    
    cv2.imwrite('{}{}'.format(image_path2, i), img)
    