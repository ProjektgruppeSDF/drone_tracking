from detection.display_detection import display_image_with_detection, displayImage

class ImageProcessor:

    def __init__(self, camera, detector, tracker, videosaver, target_loss_monitorer) -> None:
        self.camera = camera
        self.detector = detector
        self.tracker = tracker
        self.videosaver = videosaver
        self.target_loss_monitorer = target_loss_monitorer

        self.last_results = ()

    def process_frame(self, mode):
        image, time = self.camera.capture_image()

        try:
            ptz = self.camera.get_camera_ptz_orientation()
        except:
            return self.last_results
        
        detection_results = self.detector.detect(image)

        if detection_results.exists:
            display_image_with_detection(image, detection_results, self.target_loss_monitorer)
            tracking_result = self.tracker.track(detection_results, time)
            self.target_loss_monitorer.target_detection(time)
            self.camera.move_camera(tracking_result, ptz["zoom"])
        else:
            displayImage(image, mode, self.target_loss_monitorer)

        self.videosaver.write(image)

        self.last_results = (detection_results.exists, time, ptz)
        return self.last_results