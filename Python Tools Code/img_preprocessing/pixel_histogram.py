import cv2
import matplotlib.pyplot as plt

def show_histogram(image_path):
    # 이미지를 읽습니다.
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # OpenCV는 BGR 순서로 픽셀을 읽기 때문에 순서를 변경합니다.
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    # 각 채널별 히스토그램을 계산합니다.
    red_hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    green_hist = cv2.calcHist(images=[image], channels=[1], mask=None, histSize=[256], ranges=[0, 256])
    blue_hist = cv2.calcHist(images=[image], channels=[2], mask=None, histSize=[256], ranges=[0, 256])
    # gray_hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

    # 히스토그램을 그래프로 표시합니다.
    plt.figure(figsize=(10, 5))
    plt.title("Color Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixels")
    plt.plot(red_hist, color='red', label='Red channel')
    plt.plot(green_hist, color='green', label='Green channel')
    plt.plot(blue_hist, color='blue', label='Blue channel')
    # plt.plot(gray_hist, color='gray', label='Gray channel')
    plt.legend()
    plt.grid()
    plt.show()

# 실행 예
image_path = "./KneeXray/train/0/9001695L.png"
# image_path = "./5a28d27ae4b028f6846ae00a.dcm_left.png"
show_histogram(image_path)