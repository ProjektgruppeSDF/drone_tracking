from config.global_config import disable_proxy_server_for_camera
from detection.detection import Detector
from detection.detection_model_factory import * 
from tracking.tracker import Tracker
from camera.camera import Camera
from videosave.videosaver import Videosaver
from tracking.target_loss_monitor import TargetLossMonitorer
from shutdown.shutdown import set_exit_strategy
from processor_pipeline.image_processor import ImageProcessor



if __name__ == "__main__":

    disable_proxy_server_for_camera()
    set_exit_strategy()

    
    
    camera = Camera()
    detection_model = get_rtdetr_model_drone()
    detector = Detector(detection_model)
    tracker = Tracker()
    target_loss_monitorer = TargetLossMonitorer()
    videosaver = Videosaver()
    image_processor = ImageProcessor(camera, detector, tracker, videosaver, target_loss_monitorer)


    while True:

        # Scan Modus
        while True:
            detection_exists, time, ptz = image_processor.process_frame("Scan")
            if not detection_exists:
                camera.scan(ptz["tilt"])           
            else:
                break

        # Tracking Modus
        while True:
            detection_exists, time, ptz = image_processor.process_frame("Tracking")
            if not detection_exists:
                target_loss_monitorer.no_target_detection(time)
                if target_loss_monitorer.is_target_lost:
                    tracker.reinitialise()
                    break

    
        