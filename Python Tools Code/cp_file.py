""" import shutil

img_list = ['0/9488401L.png', '1/9967294R.png', '2/9792506L.png', '3/9669124L.png', '4/9559547R.png']
# img_list = ['9488401L.png', '9967294R.png', '9792506L.png', '9669124L.png', '9559547R.png']

for file_name in img_list:
    original_img_dir = f'./KneeXray/test/{file_name}'
    densenet_161_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/densenet_161/{file_name}'
    efficientnet_b5_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/efficientnet_b5/{file_name}'
    efficientnet_v2_s_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/efficientnet_v2_s/{file_name}'
    regnet_y_8gf_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/regnet_y_8gf/{file_name}'
    resnet_101_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/resnet_101/{file_name}'
    resnext_50_32x4d_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/resnext_50_32x4d/{file_name}'
    wide_resnet_50_2_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/wide_resnet_50_2/{file_name}'
    shufflenet_v2_x2_0_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/shufflenet_v2_x2_0/{file_name}'
    ensemble_cam_dir = f'./Grad CAM (Model)/Image Size Optimization/ensemble_cam/{file_name}'
    
    
    img_dir_list = [
        original_img_dir,
        densenet_161_cam_dir,
        efficientnet_b5_cam_dir,
        efficientnet_v2_s_cam_dir,
        regnet_y_8gf_cam_dir,
        resnet_101_cam_dir,
        resnext_50_32x4d_cam_dir,
        wide_resnet_50_2_cam_dir,
        shufflenet_v2_x2_0_cam_dir,
        ensemble_cam_dir
    ]
    
    model = [
        'original',
        'densenet_161',
        'efficientnet_b5',
        'efficientnet_v2_s',
        'regnet_y_8gf',
        'resnet_101',
        'resnext_50_32x4d',
        'wide_resnet_50_2',
        'shufflenet_v2_x2_0',
        'ensemble'
    ]
        
    for img_dir, model in zip(img_dir_list, model):
        save_dir = f"./Grad CAM (Model)/Fig. 6-10/Optimization/{file_name.split('.')[0]}_{model}.png"
        shutil.copyfile(img_dir, save_dir) """
        
        
import shutil
import os

src_dirs = {
    "Image Size Original": "Image Size Original",
    "Image Size Optimization": "Image Size Optimization"
}

image_files = {
    "0": "9137709R.png",
    "1": "9055361R.png",
    "2": "9057327R.png",
    "3": "9011053L.png",
    "4": "9504935L.png"
}

model_architectures = ["densenet_161", "efficientnet_b5", "efficientnet_v2_s", "regnet_y_8gf", "resnet_101", "resnext_50_32x4d", "shufflenet_v2_x2_0", "wide_resnet_50_2", "ensemble_cam"]

for dir_name, src_dir in src_dirs.items():
    for model in model_architectures:
        for grade, img_file in image_files.items():
            src_file_path = os.path.join("./Grad CAM/", src_dir, model, grade, img_file)
            dst_file_path = os.path.join("./Grad CAM Revision/", grade, f"{img_file.split('.')[0]}_{model}.png")

            shutil.copy2(src_file_path, dst_file_path)