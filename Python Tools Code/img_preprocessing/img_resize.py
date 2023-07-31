import cv2
import os

for la in range(0, 5):
    image_path = f'/Users/pisunwoo/Downloads/KL Grade Datasets/HH_Perfection/HH_1/{la}/'
    image_path2 = f'/Users/pisunwoo/Downloads/KL Grade Datasets/HH_Perfection/HH_1/resize/{la}/'
    img_list = os.listdir(image_path)
    png_files = [file for file in img_list if file.endswith(".png")]
    

    for i in png_files:
        img = cv2.imread('{}{}'.format(image_path, i), cv2.IMREAD_GRAYSCALE)
        img2 = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('{}{}'.format(image_path2, i), img2)