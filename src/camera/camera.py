from .camera_specs import *
from .camera_url_queries import *
from.camera_flip_monitorer import CameraFlipMonitorer
from config.global_config import camera_resolution
from .resolution import *

import math
import requests
import cv2
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        self.video = cv2.VideoCapture(query_videostream_flipped_)
        #self.video.set(cv2.CAP_PROP_OPENNI_MAX_BUFFER_SIZE, 3)
        #self.video.set(cv2.CAP_PROP_BUFFERSIZE, 10)
    
        self.camera_flip_monitorer = CameraFlipMonitorer(self._get_ptz()["pan"])
        self.y_direction = 1
        self.resolution = camera_resolution
        self.flip_faktor = 1
        self.isZooming = 0
        

    def capture_image(self):

        dt = datetime.now()
        ret, image = self.video.read()

        return image,dt
    
    def _get_ptz(self):
        response = requests.get(query_get_orientation)

        response_text = response.text

        ptz = {}
        lines = response_text.split('\n')
        for line in lines:
            if '=' in line:
                key , value = line.split('=')

                if(key == "pan" or key == "tilt" or key == "zoom"):
                    ptz[key] = float(value.strip())

        # in seltenen Fällen scheitert die Abfrage, eventuell Verbindungsprobleme?
        self._raise_exception_on_failed_query(ptz)
        
        return ptz
    
    def _raise_exception_on_failed_query(self, ptz):
        actual_keys = sorted(ptz.keys())
        expected_keys = ["pan", "tilt", "zoom"]
        if not actual_keys == expected_keys:
            raise Exception("Warnung: ptz-query gescheitert.")
    
    def get_camera_ptz_orientation(self):
        ptz = self._get_ptz()
        self.flip_faktor = self.camera_flip_monitorer.check_camera_flipped(ptz["pan"])
        return ptz

    """
    prop_factor_velocity_distance: - Proportionalitätsfaktor zwischen Abweichung Bildmitte von Ziel und des Geschwindigkeitsvektors für die Kamerasteuerung
                                   - wurde experimentell bestimmt/angepasst

    acceptable_distance: - bei kleineren Abständen soll keine Kamerabwegung stattfinden, sonst wackelt die Kamera bei stehendem Ziel

    fov_ratio_factor: Geschwindigkeit der Kamerabewegung muss abhängig von Zoom sein, da mit steigendem Zoom das Sichtfeld kleiner wird
    """ 
    def move_camera(self, tracking_result,zoom):
  
        acceptable_distance = 25
        prop_factor_velocity_distance = 1/5
        fov_ratio_factor = get_fov_ratio_factor(zoom)

        center_pixel = get_center_pixel(self.resolution)
        deltaX = center_pixel[0] - int(tracking_result[0]) 
        deltaY = center_pixel[1]- int(tracking_result[1])
        
        if(abs(deltaX) < acceptable_distance):
            vx = 0
        else:
            vx = int(deltaX) * prop_factor_velocity_distance * fov_ratio_factor
        if(abs(deltaY) < acceptable_distance):
            vy = 0
            self.flip_faktor = 1
        else:
            vy = -int(deltaY) * prop_factor_velocity_distance * fov_ratio_factor
        url = get_query_continous_move(vx, self.flip_faktor * vy)
        requests.get(url)


    def scan(self, tilt):
        requests.get(get_query_zoom(1))
        if(tilt<-75):
            self.y_direction = -1
        elif(tilt>-10):
            self.y_direction = 1

        url = get_query_continous_move(34, self.y_direction*-5)
        requests.get(url)

    def move_to_default_position():
        print("move_to_default_position")
        requests.get(get_query_continous_move(0, 0))
        requests.get(get_query_absolute_pan(0))
        requests.get(get_query_absolute_tilt(0))
        requests.get(get_query_zoom(1))
    
    def zoom(self,detection_results):
        if self.isZooming == 0 :
            laengeX = detection_results.x2 -detection_results.x1
            laengeY = detection_results.y2 -detection_results.y1
            diagonale = math.sqrt(laengeX * laengeX + laengeY * laengeY)

            if diagonale <  get_desired_diagonal_minlength(self.resolution):
                url = get_query_relative_zoom(50)
                requests.get(url)
            elif diagonale > get_desired_diagonal_maxlength(self.resolution) :
                #rauszoomen
                url = get_query_relative_zoom(-100)
                requests.get(url)
            self.isZooming = 2
        else:
            self.isZooming = self.isZooming -1

        
