import os
import time
from detection.detection import Detector
from detection.detection_config import yolo_model, rtdetr_model
from detection.display_detection import display_image_with_detection
from tracking.tracker import Tracker
from camera.camera import Camera
from videosave.videosaver import Videosaver


if __name__ == "__main__":

    os.environ["NO_PROXY"] = "192.168.11.103"

    camera = Camera()
    detector = Detector(yolo_model)
    tracker = Tracker()
    videosaver = Videosaver()
    

    while True:
        image,dt = camera.capture_image()
        camera_orientation = camera.get_camera_orientation()
        detection_results = detector.detect(image)
        display_image_with_detection(image, detection_results)
        videosaver.write(image)
        tracking_result =  tracker.track(detection_results,dt,camera_orientation)
        camera.move_camera(tracking_result)
        