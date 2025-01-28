import cv2 as cv
import cvzone
import pickle
import numpy as np

w, h = 35, 80

cap = cv.VideoCapture("data/video5.mp4")

# Define output video parameters
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))
output_video = "parking_space_counter.mp4"

# Define VideoWriter
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

with open("carParkPos2", "rb") as f:
    posList = pickle.load(f)

def checkParkingSpace(imgPro):
    spaceCount = 0

    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y+h, x:x+w]
        count = cv.countNonZero(imgCrop)

        if count < 400:
            color = (0, 255, 0)
            thickness = 3
            spaceCount += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv.rectangle(img, pos, (pos[0]+w, pos[1]+h), color, thickness)
        # cvzone.putTextRect(img, str(count), (x, y+h - 3), scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {spaceCount}/{len(posList)}', (470, 230), scale=3, thickness=3, offset=4, colorR=(0, 200, 0))

while True:
    if cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT):
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)

    succ, img = cap.read()
    if not succ:
        break

    # image processing
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (3, 3), 1)
    imgTresh = cv.adaptiveThreshold(imgBlur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv.medianBlur(imgTresh, 5)
    kernel = np.ones((3,3), np.int8)
    imgDialate = cv.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDialate)

    out.write(img)

    cv.imshow("img", img)
    if cv.waitKey(33) & 0xFF==ord('q'):
        break