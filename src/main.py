import os
from detection.detection import Detector
from detection.detection_model_factory import get_yolo_model_person, get_yolo_model_drone_simple, get_rtdetr_model_person, get_rtdetr_model_drone_simple, get_yolo_model_drone_good
from detection.display_detection import display_image_with_detection, displayImage
from tracking.tracker import Tracker
from camera.camera import Camera
from videosave.videosaver import Videosaver
from tracking.target_loss_monitor import TargetLossMonitorer
from shutdown.shutdown import set_exit_strategy




if __name__ == "__main__":

    os.environ["NO_PROXY"] = "192.168.11.103"

    set_exit_strategy()

    
    
    camera = Camera()
    detection_model = get_yolo_model_drone_good()
    detector = Detector(detection_model)
    tracker = Tracker()
    target_loss_monitorer = TargetLossMonitorer()
    videosaver = Videosaver()
    
    


    while True:

        #Scan Modus
        print("Starte Scan Modus")
        while True:
            image,time = camera.capture_image()
            ptz = camera.get_camera_ptz_orientation()
            detection_results = detector.detect(image)
            if(not detection_results.exists):
                camera.scan(ptz["tilt"])
                displayImage(image,"Scan Modus")
                videosaver.write(image)
            else:
                display_image_with_detection(image, detection_results)
                tracking_result =  tracker.track(detection_results,time)
                camera.move_camera(tracking_result,ptz["zoom"])
                videosaver.write(image)
                break
                
        
        #Tracking Modus
        print("Starte Tracking Modus")
        while True:
            image,time = camera.capture_image()
            ptz = camera.get_camera_ptz_orientation()
            detection_results = detector.detect(image)
            if(detection_results.exists):
                display_image_with_detection(image, detection_results)
                tracking_result =  tracker.track(detection_results,time)
                target_loss_monitorer.target_detection(time)
                camera.move_camera(tracking_result,ptz["zoom"])
            else:  
                displayImage(image,"Tracking Modus")
                target_loss_monitorer.no_target_detection(time)
                if target_loss_monitorer.is_target_lost:
                    tracker.reinitialise()
                    break          
                
            videosaver.write(image)

    
        