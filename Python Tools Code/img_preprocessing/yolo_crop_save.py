import os
import shutil
import cv2
from ultralytics import YOLO

# Load a model
model = YOLO('./best.pt')  # load a custom model

input_path = './HH_1/4/'
output_path = './crop/4/'

path = os.listdir(input_path)
for img in path:
    image = os.path.join(input_path, img)
    results = model(image)  # predict on an image
    
    for box in results:  
        box = box.cpu().numpy().boxes.xyxy[0]
        minx = int(box[0])
        miny = int(box[1])
        maxx = int(box[2])
        maxy = int(box[3])
        
        image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        crop = image[miny:maxy,minx:maxx]
        cv2.imwrite(os.path.join(output_path, img), crop)