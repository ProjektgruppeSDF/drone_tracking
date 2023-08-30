from .camera_specs import *
from .camera_url_queries import query_videostream_flipped_, query_get_orientation, get_query_continous_move
from.camera_flip_monitorer import CameraFlipMonitorer


import requests
import cv2
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        self.video = cv2.VideoCapture(query_videostream_flipped_)
        self.camera_flip_monitorer = CameraFlipMonitorer(self._get_ptz()["pan"])
        self.y_direction = 1
        

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

                # für Debugging: Es kam vermutlich einmal keine response im erwarteten Format zurück
                print(lines)
                print("\n")


                if(key == "pan" or key == "tilt" or key == "zoom"):
                    ptz[key] = float(value.strip())

        return ptz
    
    def get_camera_ptz_orientation(self):
        ptz = self._get_ptz()
        if(self.camera_flip_monitorer.check_camera_flipped(ptz["pan"])):
            # siehe Kommentar in camer_flip_monitorer.py
            url = get_query_continous_move(0, 0)
            requests.get(url) 
        return ptz

# TODO: der Faktor 1/25 sollte zoomabhängig gewählt sein
    def move_camera(self, tracking_result,zoom):
        #Auflösung ist 1920x1080 und 960,540 ist der Mittelpunkt des Bildes
        abweichungX = 960 - int(tracking_result[0]) 
        abweichungy = 540 - int(tracking_result[1])
        
        #Kamerabewegung durch Richtung/Geschwindigkeit
        #Kamerabewgung abhängig von Abstand zum Mittelpunkt des Bildes sowie des Zooms
        
        vx = -(int(abweichungX) / 25)
        vy = (int(abweichungy) / 25 )
        url = get_query_continous_move(vx, vy)
        requests.get(url)


    def move_scan_camera(self, tilt):

        if(tilt<-75):
            self.y_direction = -1
        elif(tilt>-10):
            self.y_direction = 1

        url = get_query_continous_move(20, self.y_direction*-5)
        requests.get(url)

        
