
import requests


from detection.detection_result import DetectionBox



class Tracker:
    
    def track(self, detection_results):
        #xCenter = 
        #boundingCenter = tracking_point(detection_results.confidence)
        try: 
            detect1 = detection_results[0]
            detectX = (detect1.x2 + detect1.x1) / 2
            detectY = (detect1.y2 + detect1.y1) / 2
            print(detectX, detectY)
            print(detect1.x1,detect1.x2,detect1.y1,detect1.y2)
        except: 
            print("list index out of range")
        #try: 
 
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rpan=5'
            #response = requests.get(url)
        #except: 
            #print("request gescheitert")
        #pass