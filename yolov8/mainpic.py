# cv2: the package that allows screen opening, video playing and drawing bounding boxes
import numpy as np
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
# model = YOLO("last.pt")
results = model(['collected_images/n.jpg'])
for result in results:
    pass

