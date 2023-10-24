import cv2
import uuid
import os
# import PyQt5

import time
# connect to webcam, number differs for os, should pop up screen
# print(PyQt5.__version__)
collected_images_folder = "collected_images"
labels = ['fuck_you']
labels = ['necklace']
labels = ['good']
for label in labels:
    if not os.path.exists(collected_images_folder):
        os.makedirs(collected_images_folder)
    labeled_images_folder = os.path.join(collected_images_folder,label)
    if not os.path.exists(labeled_images_folder):
        os.makedirs(labeled_images_folder)
cap = cv2.VideoCapture(0)
for label in labels:
    print("Collecting image for: " + label)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Img", frame)

        key = cv2.waitKey(1)

        # 'q'
        if key == 113:
            break

        # 'ENTER'
        if key == 13:
            imgname = os.path.join(
                'collected_images', label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imgname, frame)

cap.release()
cv2.destroyWindow('frame')
cv2.waitKey(1)
print('Done')
