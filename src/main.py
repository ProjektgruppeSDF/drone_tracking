import os
from modes.modes import ProgramMode, Modes
from detection.detection import Detector
from detection.detection_model_factory import get_yolo_model_person, get_yolo_model_drone_simple, get_rtdetr_model_person, get_rtdetr_model_drone_simple, get_yolo_model_drone_good
from detection.display_detection import display_image_with_detection, displayImage
from tracking.tracker import Tracker
from camera.camera import Camera
from videosave.videosaver import Videosaver
from tracking.target_loss_monitor import TargetLossMonitorer



if __name__ == "__main__":

    os.environ["NO_PROXY"] = "192.168.11.103"

    program_mode = ProgramMode(Modes.SCAN_MODE)
    
    camera = Camera()
    detection_model = get_yolo_model_person()
    detector = Detector(detection_model)
    tracker = Tracker()
    target_loss_monitorer = TargetLossMonitorer()
    videosaver = Videosaver()

    while True:

        #Scan Modus
        while True:
            image,dt = camera.capture_image()
            ptz = camera.get_camera_ptz_orientation()
            detection_results = detector.detect(image)
            if(detection_results.exists):
                display_image_with_detection(image, detection_results)
                tracking_result =  tracker.track(detection_results,dt)
                camera.move_camera(tracking_result,ptz["zoom"])
                break
            else:
                camera.move_scan_camera(ptz["tilt"])
                displayImage(image)
                videosaver.write(image)

        #Tracking Modus
        while True:
            image,dt = camera.capture_image()
            ptz = camera.get_camera_ptz_orientation()
            detection_results = detector.detect(image)
            if(not detection_results.exists):
                target_loss_monitorer.no_target_detection(dt)
                if target_loss_monitorer.is_target_lost:
                    tracker.reintialise()
                    break
            elif(detection_results.exists):            
                display_image_with_detection(image, detection_results)
                tracking_result =  tracker.track(detection_results,dt)
                target_loss_monitorer.target_detection(dt)
                camera.move_camera(tracking_result,ptz["zoom"])
            videosaver.write(image)

    
        