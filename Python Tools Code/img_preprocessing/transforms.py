import cv2
import os
import albumentations as A


for cls in range(5):
    image_path = f'../HH_1/{cls}/'
    image_path2 = f'../HH_1/augmentation_RC/{cls}/'
    img_list = os.listdir(image_path)

    for i in img_list:
        img = cv2.imread('{}{}'.format(image_path, i), cv2.IMREAD_GRAYSCALE)
                
        transform = A.Compose([
                        # A.GridDistortion(interpolation=cv2.INTER_CUBIC, p=1),
                        # A.ElasticTransform(interpolation=cv2.INTER_CUBIC, p=1),
                        # A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.1, p=1),
                        # A.CLAHE(p=1),
                        A.RandomCrop(height=int(img.shape[1]*0.70), width=int(img.shape[0]*0.90), p=1),
                        # A.GaussNoise(var_limit=(0, 50), p=1),
                        # A.RandomGamma(p=1),
                        # A.HorizontalFlip(p=1),
                        # A.Rotate(limit=20, p=1),
                        ])

        img2 = transform(image=img)['image']

        cv2.imwrite('{}{}'.format(image_path2, i), img2)