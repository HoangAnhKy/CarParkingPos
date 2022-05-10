import cv2
import pickle

width, height = 120, 50
width_img, height_img = 1370, 790

try:
    with open('CarParkingPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkingPos', 'wb') as f:
        pickle.dump(posList, f)


while True:
    key = cv2.waitKey(0)
    if key > 0:  # exit on ESC
        break
    img = cv2.imread('Park.jpg')
    img = cv2.resize(img, (width_img, height_img))

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width,
                      pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)
