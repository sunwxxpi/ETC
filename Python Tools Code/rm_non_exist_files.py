import os
import os.path

# 이미지와 레이블 파일이 저장된 경로 설정
images_dir = './dataset/SyRIP_YOLO/train_1200/images/'
labels_dir = './dataset/SyRIP_YOLO/train_1200/labels/'

# 경로에 있는 모든 파일 이름 불러오기
image_files = os.listdir(images_dir)
label_files = os.listdir(labels_dir)

# images 디렉토리에서 파일 읽어오기
for image_file in image_files:
    # 파일명 중 확장자를 제외한 부분만 추출
    base_filename = os.path.splitext(image_file)[0]

    # label_files의 확장자를 제외한 부분 만 추출하고 .txt를 붙여 파일명을 구성
    label_file = base_filename + '.txt'

    # label_files 리스트에 같은 이름의 파일이 없는 경우
    if label_file not in label_files:
        # 이미지 파일 삭제
        os.remove(os.path.join(images_dir, image_file))
        print(f"Deleted: {os.path.join(images_dir, image_file)}")