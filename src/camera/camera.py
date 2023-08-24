

import requests
import cv2
import numpy as np
import os 
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        #self.video = requests.get('http://192.168.11.103/axis-cgi/mjpg/video.cgi', stream=True)
        #if not self.video.status_code == 200:
        #    print(self.video.status_code)
        #    raise Exception("Kamera nicht erreichbar.")
        #self.bytes_ = bytes()
        self.video = cv2.VideoCapture('rtsp://192.168.11.103/axis-media/media.amp?videocodec=h264&resolution=800x450&rotation180')

    def capture_image(self):
        dt = datetime.now()
        ret,image = self.video.read()
        url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?query=position)'
        response = requests.get(url)

        #Positiond er Kamera auslesen
        response_text = response.text

        values = []
        lines = response_text.split('\n')
        for line in lines:
            if '=' in line:
                key , value = line.split('=')
                values.append(value.strip())
            if(key == 'zoom'):
                break


        return image,dt,values
    

    def move_camera(self, tracking_result):
        try:
            abweichungX = 400 - tracking_result[0] #Auflösung ist 800x450 und 400,225 ist der Mittelpunkt des Bildes
            abweichungy = 225 - tracking_result[1]
            #Kamerabewegung mit relativer Position
            #bewegungX = -(abweichungX / 60)
            #bewegungY = -(abweichungy /60)
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rpan='+str(bewegungX)
            #response = requests.get(url)
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rtilt='+str(bewegungY)
            #response = requests.get(url)
            #Kamerabewegung durch Richtung/Geschwindigkeit
            bewegungX = -(abweichungX / 8)
            bewegungY = abweichungy /8
            url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?continuouspantiltmove='+str(int(bewegungX))+','+str(int(bewegungY))
            response = requests.get(url)
 
        except:
            print("keine bounding box")
        pass