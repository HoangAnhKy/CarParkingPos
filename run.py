import cv2
import pickle
import cvzone
import numpy as np


cap = cv2.VideoCapture('Video_Baidoxe.mp4')


with open('CarParkingPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 120, 50
width_img, height_img = 1370, 790


def checkParkingSpace(imgPro):

    # Đếm các vị trí
    spaceCounter = 0
    errorCounter = 0

    # Điều kiện nhận dạng
    condition_permit = 300
    condition_warning = 800  # 1400

    # khai báo màu (RGP), màu bị đảo ngược R với P
    color_green = (0, 255, 0)
    color_blue_reverse_to_red = (0, 0, 255)
    color_blue_reverse_to_orange = (0, 165, 255)

    for pos in posList:
        x, y = pos
        # print(x, y)
        imgCrop = imgPro[y:y + height, x:x + width]

        count = cv2.countNonZero(imgCrop)

        if count <= condition_permit:
            color = color_green
            thickness = 2
            spaceCounter += 1
        elif count < condition_warning and count > condition_permit:
            color = color_blue_reverse_to_orange
            thickness = 2
            errorCounter += 1
        else:
            color = color_blue_reverse_to_red
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width,
                      pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3),
                           scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (40, 40), scale=2,
                       thickness=2, offset=10, colorR=(0, 200, 0))
    cvzone.putTextRect(img, f'Warning: {errorCounter}/{len(posList)}', (400, 40), scale=2,
                       thickness=2, offset=10, colorR=(0, 180, 255))


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    img = cv2.resize(img, (width_img, height_img))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # chuyển màu sang màu xám
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)  # làm mờ ảnh
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)  # chuyển đổi sang đen trắng để tại các điểm sáng
    imgMedian = cv2.medianBlur(imgThreshold, 5)  # xử lý các điểm sáng
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("ParkingSpace DNTU", img)
    cv2.waitKey(1)
