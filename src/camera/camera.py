from .camera_specs import *
from .camera_url_queries import *
from.camera_flip_monitorer import CameraFlipMonitorer
from config.global_config import camera_resolution
from .resolution import get_center_pixel


import requests
import cv2
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        self.video = cv2.VideoCapture(query_videostream_flipped_)
        self.camera_flip_monitorer = CameraFlipMonitorer(self._get_ptz()["pan"])
        self.y_direction = 1
        self.resolution = camera_resolution
        self.flip_faktor = 1
        

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

# TODO: der Faktor 1/25 sollte zoomabhängig gewählt sein
    def move_camera(self, tracking_result,zoom):
      
        center_pixel = get_center_pixel(self.resolution)
        abweichungX = center_pixel[0] - int(tracking_result[0]) 
        abweichungy = center_pixel[1]- int(tracking_result[1])
        
        #Kamerabewegung durch Richtung/Geschwindigkeit
        #Kamerabewgung abhängig von Abstand zum Mittelpunkt des Bildes sowie des Zooms
        if(abs(abweichungX) < 25):
            vx = 0
        else:
            vx = (int(abweichungX) / 25)
        if(abs(abweichungy) < 25):
            vy = 0
            self.flip_faktor = 1
        else:
            vy = -(int(abweichungy) / 25 )
        url = get_query_continous_move(vx, self.flip_faktor * vy)
        requests.get(url)


    def scan(self, tilt):

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
        

        
