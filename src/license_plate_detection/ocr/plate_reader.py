#  OCR Detection
import cv2
import numpy as np
import easyocr
import re


class Plate_Reader:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu = True)
        self.plate_pattern = re.compile(r"^[A-Z]{2}[0-9]{2}[A-Z]{3}$")

    def plate_pattern(self):
        return self.plate_pattern

    def correct_plate_format(ocr_text):
        mapping_num_to_alpha = {
            '0': 'O',
            '1': 'I',
            '2': 'Z',
            '3': 'E',
            '4': 'A',
            '5': 'S',
            '6': 'G',
            '7': 'L',
            '8': 'B',
            '9': 'G'
        }

        mapping_alpha_to_num = {
            'O': '0',
            'I': '1',
            'Z': '2',
            'E': '3',
            'A': '4',
            'S': '5',
            'G': '6',
            'L': '7',
            'B': '8',
            'G': '9'
        }

        ocr_text = ocr_text.upper().replace(" ", "")
        if(len(ocr_text) != 7):
            return None

        corrected = []

        for i , ch in enumerate(ocr_text):
            if i > 2 or i >= 4:
                if ch.isdigit() and ch in mapping_num_to_alpha:
                    corrected.append(mapping_num_to_alpha[ch])
                elif ch.isalpha():
                    corrected.append(ch)
                else:
                    corrected.append(ch)
            else:
                if ch.isalpha() and ch in mapping_alpha_to_num:
                    corrected.append(mapping_alpha_to_num[ch])
                elif ch.isdigit():
                    corrected.append(ch)
                else:
                    return ""

        return "".join(corrected)
        
        
        

