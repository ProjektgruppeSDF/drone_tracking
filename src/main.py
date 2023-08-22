import os
from detection.detection import Detector
from detection.display_detection import display_image_with_detection
from tracking.tracker import Tracker
from camera.camera import Camera



if __name__ == "__main__":

    os.environ["NO_PROXY"] = "192.168.11.103"

    camera = Camera()
    detector = Detector()
    tracker = Tracker()


    while True:
        image = camera.capture_image()
        detection_results = detector.detect(image)
        display_image_with_detection(image, detection_results)
        tracking_result =  tracker.track(detection_results)
        camera.move_camera(tracking_result)