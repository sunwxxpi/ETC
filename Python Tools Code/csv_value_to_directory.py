import csv
import os
import shutil

csv_path = './old KL_Labels.csv'  # csv 파일 경로
img_dir = './img_data/'  # 이미지 데이터 경로

with open(csv_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Header 줄 건너뛰기

    for row in reader:
        file_name = row[1]  # File
        kl_grade_left = row[2]  # KL Grade Left
        kl_grade_right = row[3]  # KL Grade Right

        # 이미지 파일 경로 생성
        img_left_file_path = os.path.join(img_dir, f"{file_name}_left.png")
        img_right_file_path = os.path.join(img_dir, f"{file_name}_right.png")

        # 대상 폴더 경로 생성
        target_folder_left = f"{kl_grade_left}"
        target_folder_right = f"{kl_grade_right}"

        # 파일이 이미지 데이터 디렉토리에 있는지 확인
        if os.path.exists(img_left_file_path) and os.path.exists(img_right_file_path):
            # 대상 폴더 경로 생성 및 복사
            os.makedirs(target_folder_left, exist_ok=True)
            os.makedirs(target_folder_right, exist_ok=True)

            shutil.copy(img_left_file_path, os.path.join(target_folder_left, f"{file_name}_left.png"))
            shutil.copy(img_right_file_path, os.path.join(target_folder_right, f"{file_name}_right.png"))