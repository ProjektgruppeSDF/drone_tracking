from .camera_url_queries import query_videostream_flipped_, query_get_orientation, get_query_continous_move

import requests
import cv2
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        self.video = cv2.VideoCapture(query_videostream_flipped_)

    def capture_image(self):
        dt = datetime.now()
        ret,image = self.video.read()
        return image,dt
    
    def get_camera_ptz_orientation(self):
        response = requests.get(query_get_orientation)

        response_text = response.text

        ptz = {}
        lines = response_text.split('\n')
        for line in lines:
            if '=' in line:
                key , value = line.split('=')
                if(key == "pan" or key == "tilt" or key == "zoom"):
                    ptz[key] = float(value.strip())
        return ptz

    def move_camera(self, tracking_result,zoom):
        try:
            #Auflösung ist 800x450 und 400,225 ist der Mittelpunkt des Bildes
            abweichungX = 400 - tracking_result[0] 
            abweichungy = 225 - tracking_result[1]
            #Kamerabewegung mit relativer Position
            #bewegungX = -(abweichungX / 60)
            #bewegungY = -(abweichungy /60)
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rpan='+str(bewegungX)
            #response = requests.get(url)S
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rtilt='+str(bewegungY)
            #response = requests.get(url)
            #Kamerabewegung durch Richtung/Geschwindigkeit
            #Kamerabewgung abhängig von Abstand zum Mittelpunkt des Bildes sowie des Zooms
            bewegungX = -(abweichungX / (16 * float(zoom)))
            bewegungY = (abweichungy /(16 * float(zoom)))
            url = get_query_continous_move(bewegungX, bewegungY)
            print(zoom)
            print(url)
            response = requests.get(url)
 
        except:
            print("keine bounding box")
        pass