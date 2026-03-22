import cv2
import numpy as np
import easyocr
import re
from collections import defaultdict, deque

class Plate_History:
    def __init__(self):
        self.plate_histroy = defaultdict(lambda: deque(maxlen=10))
        self.plate_final = {}

    def get_box_id(self, x1, y1, x2, y2):
        new_x1 = int(x1 / 10)
        new_y1 = int(y1 / 10)
        new_x2 = int(x2 / 10)
        new_y2 = int(y2 / 10)
        return f"{new_x1}_{new_y1}_{new_x2}_{new_y2}"

    def get_stable_plate(self, box_id , new_text):
        if new_text:
            self.plate_histroy[box_id].append(new_text)

        most_common = max(set(self.plate_histroy[box_id]), key=self.plate_histroy[box_id].count)

        self.plate_final[box_id] = most_common
        
        return self.plate_final.get(box_id, "")
    

            


