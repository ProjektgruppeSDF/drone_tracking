from ultralytics import YOLO
from ultralytics import RTDETR

import math 

from .detection_config import  classNames
from .detection_result import DetectionBox

class Detector:

    def __init__(self, model) -> None:
        self.model = model

        # wofür?
        #resultsDETR = self.modelDETR.train(data='coco8yaml', epochs=100, imgsz=640)
    


    def detect(self, img):
        results = self.model(img, stream=True)
        detection_boxes= []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                confidence = math.ceil((box.conf[0]*100))/100
                cls = int(box.cls[0])
                class_label = classNames[cls]
                detectionBox = DetectionBox(x1, y1, x2, y2, confidence, class_label)
                if(detectionBox.class_label == "person"):
                    detection_boxes.append(detectionBox)
            if(len(detection_boxes)!= 0):
                result = detection_boxes[0]
                for box in detection_boxes:
                    if(box.confidence > result.confidence):
                        result = box
                detection_boxes.clear()
                detection_boxes.append(result)
        return detection_boxes
        
    
