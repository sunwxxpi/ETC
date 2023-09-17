import os
import shutil

source_dir = './Tested on LowerLimb_4-1'

target_base_dir = './outputs/3-5/'

files = os.listdir(source_dir)

for file in files:
    file_name_without_ext = os.path.splitext(file)[0]
    
    dir_name = file_name_without_ext.split('_')[0]

    target_dir = os.path.join(target_base_dir, dir_name, 'mask')
    os.makedirs(target_dir, exist_ok=True)

    source_file_path = os.path.join(source_dir, file)
    target_file_path = os.path.join(target_dir, file)

    shutil.move(source_file_path, target_file_path)

print("Complete.")