
import requests
import numpy as np
from datetime import datetime
from datetime import timedelta


from detection.detection_result import DetectionBox



class Tracker: 
    state_covariance = np.eye(2) * 30.0 
    process_noise = np.eye(2) * 5  
    measurement_noise = np.eye(2) * 10 
    velocity = np.array([0,0]) 
    alt = np.array([-1,-1])
    pdt = datetime.date
    state = np.array([-1,-1])
    

    def __init__(self) -> None:
        self.datei = open('position.txt','r+')

    def kalman_filter(self,measurement,tdems):
        
        # Vorhersage 
        #self.velocity = (self.velocity*tdems)
        predicted_state = self.state + self.velocity
        predicted_state_covariance = self.state_covariance + self.process_noise
        
        # Filterung
        kalman_gain = predicted_state_covariance / (predicted_state_covariance + self.measurement_noise)
        updated_state = predicted_state + kalman_gain * (measurement - predicted_state)
        updated_state_covariance = (np.eye(2) - kalman_gain) * predicted_state_covariance
        
        return updated_state,updated_state_covariance

    def track(self, detection_results,dt,ausrichtung):

        results = []
        if(len(detection_results)!= 0): 
            detect1 = detection_results[0]
            detectX = (detect1.x2 + detect1.x1) / 2
            detectY = (detect1.y2 + detect1.y1) / 2
            pre = np.array([detectX,detectY])
            if(np.array_equal(self.state,[-1,-1])):
                 #initalisierung
                self.state = pre
                self.velocity = [0,0]
                self.alt = pre
                self.pdt = dt
            else:
                tde = self.pdt - dt
                tdems = int(tde/timedelta(milliseconds=1))
                self.state, self.state_covariance= self.kalman_filter(pre,tdems)

                self.velocity = (pre-self.alt) /tdems
                self.alt = pre

            results.append(pre[0])
            results.append(pre[1])
            position = [] #0 Pan 1 Tilt 2 Zoom
            position.append(float(ausrichtung[0])+results[0]/(14.5)*float(ausrichtung[2]))
            position.append(float(ausrichtung[1])+results[1]/(13.5)**float(ausrichtung[2]))
            print(position)
            self.datei.write("\n"+str(position))
            return results


