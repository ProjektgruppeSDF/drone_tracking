from dataclasses import dataclass



@dataclass
class DetectionBox:
    x1: int
    y1: int
    x2: int
    y2: int
    confidence: float
    class_label: str
