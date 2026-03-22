# Connecting Pipeline
import cv2
import numpy as np
from ultralytics import YOLO
import easyocr 
import re
from src.license_plate_detection.ocr.plate_reader import PlateReader
from src.license_plate_detection.preprocessing.plate_preprocessing import Plate_Preprocessing
from src.license_plate_detection.preprocessing.plate_history import Plate_History


best_plate_model = 'models\license_plate_best.pt'
model = YOLO(best_plate_model)
plate_reader = PlateReader()

plate_pattern =plate_reader.plate_pattern()
correct_plate_format = plate_reader.correct_plate_format() #ocr_text

# mapping = 
plate_preprocessing = Plate_Preprocessing(plate_reader , plate_pattern, correct_plate_format)

plate_history = Plate_History()


