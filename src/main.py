import os
import time
from detection.detection import Detector
from detection.display_detection import display_image_with_detection
from tracking.tracker import Tracker
from camera.camera import Camera
from datetime import datetime
import cv2


if __name__ == "__main__":

    os.environ["NO_PROXY"] = "192.168.11.103"

    camera = Camera()
    detector = Detector()
    tracker = Tracker()
    video = cv2.VideoWriter('Versuch1.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, (800,450))


    while True:
        image,dt,ausrichtung = camera.capture_image()
        detection_results = detector.detect(image)
        display_image_with_detection(image, detection_results,video)
        tracking_result =  tracker.track(detection_results,dt,ausrichtung)
        camera.move_camera(tracking_result)

        