from .camera_specs import *
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
            bewegungX = -(abweichungX / (13 * float(zoom)))
            bewegungY = (abweichungy /(13 * float(zoom)))
            print(bewegungX)
            url = get_query_continous_move(bewegungX, bewegungY)
            print(zoom)
            print(url)
            response = requests.get(url)
 
        except:
            print("keine bounding box")
        pass

    # TODO: Zusammenhang von fov und zoom_value muss bestimmt werden. Entgegen der Erwartungen ist dieser nicht linear

    def get_horizontal_fov(zoom):
        if int(zoom) != 1:
            print(zoom)
            print("ACHTUNG: Für Zoom Werte zwischen 1 und 9999 ist das fov noch nicht bekannt und die Kamerasteuerung könnte unpräzise sein. ")
            #Verwende zunächst das fov für zoom = 1
        return fov_angle_horizontal_min_zoom
        
    def get_vertical_fov(zoom):
        if int(zoom) != 1:
            print(zoom)
            print("ACHTUNG: Für Zoom Werte zwischen 1 und 9999 ist das fov noch nicht bekannt und die Kamerasteuerung könnte unpräzise sein. ")
            #Verwende zunächst das fov für zoom = 1
        return fov_angle_vertical_min_zoom

    def horizontal_degrees_per_pixel(zoom):
        return Camera.get_horizontal_fov(zoom)/image_dimension[0]

    def vertical_degrees_per_pixel(zoom):
        return Camera.get_vertical_fov(zoom)/image_dimension[1]

    def get_delta_horizontal_degrees(delta_horizontal_pixels, zoom):
        return Camera.horizontal_degrees_per_pixel(zoom) * delta_horizontal_pixels
        
    def get_delta_vertical_degrees(delta_vertical_pixels, zoom):
        return Camera.horizontal_degrees_per_pixel(zoom) * delta_vertical_pixels