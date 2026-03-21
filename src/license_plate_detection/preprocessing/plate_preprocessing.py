import cv2
import numpy as np
import re
from src.license_plate_detection.ocr.plate_reader import Plate_Reader


class Plate_Preprocessing:
    def __init__(self):
        self.reader = Plate_Reader()
        self.plate_pattern = self.reader.plate_pattern()
        self.correct_plate_format = self.reader.correct_plate_format(ocr_text)

    def recognize_plate(plate_crop):
        if plate_crop.size == 0:
            return ""

        gray = cv2.cvtColor(plate_crop , cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray , 0, 255, cv2.THRESH_OTSU)

        plate_resized = cv2.resize(thresh , None, fx = 2, fy = 2, interpolation= cv2.INTER_CUBIC)
        try :
            ocr_result = self.reader.readtext(
                plate_resized,
                details= 0,
                allowlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            )
            if len(ocr_result) > 0:
                candidate = self.correct_plate_format(ocr_result[0])
                if candidate and plate_pattern.match(candidate):
                    return candidate
            return ""
        except Exception as e:
            print(f"Error in OCR: {e}")

        return ""
            
            