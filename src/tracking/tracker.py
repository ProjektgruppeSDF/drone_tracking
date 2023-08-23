
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

    def kalman_filter(self,measurement):
        
        # Vorhersage (mit Geschwindigkeits- und Beschleunigungs-Update)
        predicted_state = self.state + self.velocity 
        predicted_state_covariance = self.state_covariance + self.process_noise
        
        # Update (Korrektur) basierend auf Messung
        kalman_gain = predicted_state_covariance / (predicted_state_covariance + self.measurement_noise)
        updated_state = predicted_state + kalman_gain * (measurement - predicted_state)
        updated_state_covariance = (np.eye(2) - kalman_gain) * predicted_state_covariance
        
        return updated_state,updated_state_covariance

    
    def track(self, detection_results):
        #xCenter = 
        #boundingCenter = tracking_point(detection_results.confidence)
        results = []
        try: 
            detect1 = detection_results[0]
            detectX = (detect1.x2 + detect1.x1) / 2
            detectY = (detect1.y2 + detect1.y1) / 2
            print(detectX, detectY)
            print(detect1.x1,detect1.x2,detect1.y1,detect1.y2)
            results.append(detectX)
            results.append(detectY)
            return results
        except: 
            print("list index out of range")
    def track2(self, detection_results,dt):

        results = []
        if(len(detection_results)!= 0): 
            detect1 = detection_results[0]
            detectX = (detect1.x2 + detect1.x1) / 2
            detectY = (detect1.y2 + detect1.y1) / 2
            print(detectX, detectY)
            print(detect1.x1,detect1.x2,detect1.y1,detect1.y2)
            pre = np.array([detectX,detectY])
            if(np.array_equal(self.state,[-1,-1])):
                 #initalisierung
                self.state = pre
                self.velocity = [0,0]
                self.alt = pre
                self.pdt = dt
            else:
                
                self.state, self.state_covariance= self.kalman_filter(pre)
                tde = self.pdt - dt
                self.velocity = (pre-self.alt) * 1000 / int(tde/timedelta(milliseconds=1))
                self.alt = pre
            print(self.velocity)

            results.append(pre[0])
            results.append(pre[1])
            print(pre[0],pre[1])
            return results


