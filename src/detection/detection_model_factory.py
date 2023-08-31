from ultralytics import YOLO, RTDETR

# object classes
class_names_coco = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

class_names_drone_only = ["drone"]

class Model():
    def __init__(self, detector, class_names, target) -> None:
        self.detector = detector
        self.class_names = class_names
        self.target = target

def get_yolo_model_person():
    yolo_model_weights = "resources/yolo-Weights/yolov8n_pretrained_on_coco.pt"
    yolo_model = YOLO(yolo_model_weights)
    return Model(yolo_model, class_names_coco, "person")



def get_rtdetr_model_person():
    rtdetr_model_weights = "resources/rtdetr-Weights/rtdetr_pretrained_on_coco.pt"
    rtdetr_model = RTDETR(rtdetr_model_weights)
    return Model(rtdetr_model, class_names_coco, "person")
   


def get_yolo_model_drone_simple():
    yolo_model_drone_weights = 'resources/yolo-Weights/yolo_trained_on_simple_drone_dataset.pt'
    yolo_model_drone = YOLO(yolo_model_drone_weights)
    return Model(yolo_model_drone, class_names_drone_only, "drone")


def get_rtdetr_model_drone_simple():
    rtdetr_model_drone_weights = 'resources/rtdetr-Weights/rtdetr_trained_on_simple_drone.pt'
    rtdetr_model_drone = RTDETR(rtdetr_model_drone_weights)
    return Model(rtdetr_model_drone, class_names_drone_only, "drone")


def get_yolo_model_drone_good():
    yolo_model_drone_weights = 'resources/yolo-Weights/yolo_trained_on_good_drone_dataset.pt'
    yolo_model_drone = YOLO(yolo_model_drone_weights)
    return Model(yolo_model_drone, class_names_drone_only, "drone")


