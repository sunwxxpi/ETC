import os, sys
import cv2
import numpy as np
import pydicom
from tqdm import tqdm
import natsort

from pydicom.pixel_data_handlers.util import apply_voi_lut, apply_modality_lut

# Reference: https://github.com/ucs198604/dicom2jpg
# Convert dcm to array
def dcm2img(dcm_path):
    ds = pydicom.dcmread(dcm_path)
    pixel_array = ds.pixel_array.astype(float)

    if 'RescaleSlope' in ds and 'RescaleIntercept' in ds:
        rescale_slope = float(ds.RescaleSlope) 
        rescale_intercept = float(ds.RescaleIntercept)
        
        pixel_array = (pixel_array) * rescale_slope + rescale_intercept
    else:
        pixel_array = apply_modality_lut(pixel_array, ds)

    if 'VOILUTFunction' in ds and ds.VOILUTFunction == 'SIGMOID':
        pixel_array = apply_voi_lut(pixel_array, ds)
    elif 'WindowCenter' in ds and 'WindowWidth' in ds:
        window_center = ds.WindowCenter
        window_width = ds.WindowWidth
        
        if type(window_center) == pydicom.multival.MultiValue:
            window_center = float(window_center[0])
        else:
            window_center = float(window_center)
            
        if type(window_width) == pydicom.multival.MultiValue:
            window_width = float(window_width[0])
        else:
            window_width = float(window_width)
            
        pixel_array = np.piecewise(
            pixel_array, 
            [pixel_array <= (window_center - (window_width) / 2), pixel_array > (window_center + (window_width) / 2)], 
            [pixel_array.min(), pixel_array.max(), lambda data: ((data - window_center + window_width / 2) / window_width * (pixel_array.max() - pixel_array.min())) + pixel_array.min()]
            )
    else:
        pixel_array = apply_voi_lut(pixel_array, ds)

    # normalize to 8 bit
    pixel_array = ((pixel_array - pixel_array.min()) / (pixel_array.max() - pixel_array.min())) * 255.0

    if 'PhotometricInterpretation' in ds and ds.PhotometricInterpretation == "MONOCHROME1":
        pixel_array = np.max(pixel_array) - pixel_array

    image = pixel_array.astype('uint8')

    return image


# Save dcm to img
def save_dcm_to_img(dcm_path):
    output_path = f"./img_data/"
    output_ext = '.png'
    
    dcm_list = os.listdir(dcm_path)
    dcm_list = natsort.natsorted(dcm_list)
    
    for dcm in tqdm(dcm_list, unit='Image'):
        # Convert dcm to image
        dcm_file = os.path.join(dcm_path, dcm)
        image = dcm2img(dcm_file)

        # Save iamge
        dcm_base_name = os.path.splitext(dcm)[0]
        output_img_path = os.path.join(output_path, dcm_base_name) + output_ext
        
        cv2.imwrite(output_img_path, image)
    
    return True


if __name__=='__main__':
    save_dcm_to_img('/Users/pisunwoo/Project Code/ETC/Python Tools Code/dcm_data/')