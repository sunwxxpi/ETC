import os

# img_path = "./detect/4/crops/left_knee/"
img_path = "./detect/4/crops/right_knee/"

img_list = os.listdir(img_path)

for img in img_list:
    img_base_name = os.path.splitext(img)[0]

    before_path = os.path.join(img_path, img)
    # after_path = os.path.join('./HH_1/4/', f'{img_base_name}_left.jpg')
    after_path = os.path.join('./HH_1/4/', f'{img_base_name}_right.jpg')

    os.rename(before_path, after_path)
    
    print('Success.')