import cv2 as cv
import pickle

w, h = 35, 80

try:
    with open("carParkPos2", "rb") as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(events, x, y, flags, params):

    if events == cv.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    if events == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1+w and y1 < y < y1+h:
                posList.pop(i)

    with open("carParkPos2", "wb") as f:
        pickle.dump(posList, f)


while True:
    img = cv.imread("data/parking_space_counter.png")

    for pos in posList:
        cv.rectangle(img, pos, (pos[0]+w, pos[1]+h), (255, 0, 255), 2)

    cv.imshow("img", img)
    cv.setMouseCallback("img", mouseClick)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
