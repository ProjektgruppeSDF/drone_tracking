import os
import time
from detection.detection import Detector
from detection.detection_model_factory import get_yolo_model_person, get_yolo_model_drone, get_rtdetr_model_person, get_rtdetr_model_drone
from detection.display_detection import display_image_with_detection
from tracking.tracker import Tracker
from camera.camera import Camera
from videosave.videosaver import Videosaver



if __name__ == "__main__":

    os.environ["NO_PROXY"] = "192.168.11.103"

    detection_model = get_yolo_model_person()

    camera = Camera()
    detector = Detector(detection_model)
    tracker = Tracker()
    videosaver = Videosaver()
    

    while True:
        image,dt = camera.capture_image()
        ptz = camera.get_camera_ptz_orientation()
        detection_results = detector.detect(image)
        display_image_with_detection(image, detection_results)
        videosaver.write(image)
        tracking_result =  tracker.track(detection_results,dt)
        camera.move_camera(tracking_result,ptz["zoom"])
        