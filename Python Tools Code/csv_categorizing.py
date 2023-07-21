import os
import shutil
import pandas as pd

csv_file = './VinDr-SpineXR/annotations/test.csv'
data = pd.read_csv(csv_file)

image_directory = './VinDr-SpineXR/test_images_jpg'

unique_lesion_types = data['lesion_type'].unique()

for lesion_type in unique_lesion_types:
    os.makedirs(lesion_type, exist_ok=True)
    
    lesion_data = data[data['lesion_type'] == lesion_type]
    
    for index, row in lesion_data.iterrows():
        image_id = row['image_id'] + '.jpg'
        src = os.path.join(image_directory, image_id)
        dst = os.path.join(lesion_type, image_id)
        shutil.copy(src, dst)
    
    lesion_data.to_csv(os.path.join(lesion_type, f"{lesion_type}_data.csv"), index=False)
    print(f"{lesion_type} Finished.")