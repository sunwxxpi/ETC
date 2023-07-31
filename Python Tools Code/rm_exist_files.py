import os
import os.path

# 이미지와 레이블 파일이 저장된 경로 설정
HH_1_path = '/Users/pisunwoo/Downloads/KL Grade Datasets/HH_1/Ver.2/HH_1/4/'
not_use_path = '/Users/pisunwoo/Downloads/KL Grade Datasets/HH_1/Ver.1/Not Use_grade/4/'

# 경로에 있는 모든 파일 이름 불러오기
hh_1_list = os.listdir(HH_1_path)
not_use_list = os.listdir(not_use_path)

# images 디렉토리에서 파일 읽어오기
for not_use in not_use_list:
    # 파일명 중 확장자를 제외한 부분만 추출
    # not_use_list 리스트에 같은 이름의 파일이 없는 경우
    if not_use in hh_1_list:
        # 이미지 파일 삭제
        os.remove(os.path.join(HH_1_path, not_use))
        print(f"Deleted: {os.path.join(HH_1_path, not_use)}")