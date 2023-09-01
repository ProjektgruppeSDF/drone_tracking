from .detection_result import DetectionBox, getDetectionBox

class Detector:

    def __init__(self, model) -> None:
        self.model = model

    def detect(self, img):
        results = self.model.detector(img, stream=True)
        detection_boxes= []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                detectionBox = getDetectionBox(box, self.model.class_names)
                if((detectionBox.class_label == self.model.target) & (float(detectionBox.confidence) > float(3/10))):
                    detection_boxes.append(detectionBox)
            if(self.nothing_detected(detection_boxes)):
                return DetectionBox(False, 0, 0, 0, 0, 0, "")
            else:
                return self.get_result_with_highest_confidence(detection_boxes)
                
    def nothing_detected(self, detection_boxes):
        return len(detection_boxes)== 0
    
    def get_result_with_highest_confidence(self, detection_boxes):
        result = detection_boxes[0]
        for detection_box in detection_boxes:
            if(detection_box.confidence > result.confidence):
                result = detection_box
        return result
    
        
    
