from detection.detection_config import source
from detection.detection import Detector
from detection.display_detection import display_image_with_detection
from tracking.tracker import Tracker
from camera.camera import Camera



if __name__ == "__main__":

    camera = Camera()
    detector = Detector()
    tracker = Tracker()


    while True:
        image = camera.capture_image()
        detection_results = detector.detect(image)
        display_image_with_detection(image, detection_results)
        tracking_result =  tracker.track(detection_results)
        camera.move_camera(tracking_result)