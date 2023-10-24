import numpy as np
import cv2
from ultralytics import YOLO
import torch

model = YOLO("yolov8n.pt")
# print(dir(model))
# cap = cv2.VideoCapture("collected_images/mi.MOV")
# ret, frame = cap.read()
# results = model(frame, device="mps")
# result = results[0]
# print(result.names)

model.train(data = 'dataset.yaml', epochs = 3, imgsz = 1200, device = "mps")