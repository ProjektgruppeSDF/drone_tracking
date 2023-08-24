from dataclasses import dataclass
from .detection_config import classNames
import math


@dataclass
class DetectionBox:
    exists: bool
    x1: int
    y1: int
    x2: int
    y2: int
    confidence: float
    class_label: str


def getDetectionBox(box):
    x1, y1, x2, y2 = box.xyxy[0]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    confidence = math.ceil((box.conf[0]*100))/100
    cls = int(box.cls[0])
    class_label = classNames[cls]
    return DetectionBox(True, x1, y1, x2, y2, confidence, class_label)