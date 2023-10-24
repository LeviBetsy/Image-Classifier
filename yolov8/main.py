# cv2: the package that allows screen opening, video playing and drawing bounding boxes
import numpy as np
import cv2
from ultralytics import YOLO
# import torch

# model = YOLO("yolov8n.pt")
# model = YOLO("last.pt")
model = YOLO("best.pt")     
cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture("collected_images/mi.MOV")
# # cap = cv2.imread("collected_images/n.jpg")
# ret, frame = cap.read()
# results = model(frame, device="mps")
# result = results[0]
# print(result.names)

while True:
    ret, frame = cap.read()
    # if there are no more frame: quit. For videos
    if not ret:
        break

    # running using gpu
    results = model(frame, device="mps")
    result = results[0]


    # convert bounding boxes x,y to integers
    # in a big project, create class, class methods to get these easier
    classes = np.array(result.boxes.cls.cpu(), dtype="int")
    bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
    for cls, bbox in zip(classes, bboxes):
        # print(bbox)
        (x, y, x2, y2) = bbox
        cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 225), 2)
        cv2.putText(frame, result.names[cls], (x, y + 10),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 225), 2)

    cv2.imshow("Img", frame)

    # wait key is waiting for a key to be pressed, if there is no pressed key then it returns false
    # the number inside iis the amount of milisecond it will wait for the key
    # if number is <= 0: wait for key indefinitely
    # in this case, if it doesn't see a key then imshow can move on to the next frame.
    # t allows a time window for a pressed key
    key = cv2.waitKey(1)

    # if press key == 13 (aka ENTER): stop
    if key == 13 or key == 113:
        break

# # so another program can use the video
# cap.release()
# cv2.destroyAllWindows()
