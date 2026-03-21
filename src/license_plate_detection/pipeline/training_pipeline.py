# Connecting Pipeline
import cv2
import numpy as np
from ultralytics import YOLO
import easyocr 
import re
from src.license_plate_detection.ocr.plate_reader import PlateReader
from collections import defaultdict, deque


best_plate_model = 'models\license_plate_best.pt'
model = YOLO(best_plate_model)
plate_reader = PlateReader()

plate_pattern =plate_reader.plate_pattern()

# mapping = 



