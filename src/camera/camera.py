from .camera_url_queries import camera_videostream_flipped_query, camera_orientation_query, camera_continous_move_query

import requests
import cv2
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        self.video = cv2.VideoCapture(camera_videostream_flipped_query)

    def capture_image(self):
        dt = datetime.now()
        ret,image = self.video.read()
        return image,dt
    
    def get_camera_ptz_orientation(self):
        response = requests.get(camera_orientation_query)

        response_text = response.text

        ptz = []
        lines = response_text.split('\n')
        for line in lines:
            if '=' in line:
                key , value = line.split('=')
                ptz.append(value.strip())
            if(key == 'zoom'):
                break
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
            #response = requests.get(url)
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rtilt='+str(bewegungY)
            #response = requests.get(url)
            #Kamerabewegung durch Richtung/Geschwindigkeit
            #Kamerabewgung abhängig von Abstand zum Mittelpunkt des Bildes sowie des Zooms
            bewegungX = -(abweichungX / (8 * zoom))
            bewegungY = (abweichungy /(8 * zoom))
            url = camera_continous_move_query+str(int(bewegungX))+','+str(int(bewegungY))
            response = requests.get(url)
 
        except:
            print("keine bounding box")
        pass