
import numpy as np
from datetime import datetime
from datetime import timedelta

from camera.camera import Camera





class Tracker: 
    state_covariance = np.eye(2) * 15.0 
    process_noise = np.eye(2) * 5  
    measurement_noise = np.eye(2) * 10 
    velocity = np.array([0,0]) 
    alt = np.array([-1,-1])
    pdt = datetime.date
    state = np.array([-1,-1])
    

    def __init__(self) -> None:
        self.datei = open('position.txt','a')

    def kalman_filter(self,measurement,tdems):
        
        # Vorhersage 
        self.velocity[0] = self.velocity[0]*tdems
        self.velocity[1] = self.velocity[1]*tdems
        predicted_state = self.state + self.velocity
        predicted_state_covariance = self.state_covariance + self.process_noise
        
        # Filterung
        kalman_gain = predicted_state_covariance / (predicted_state_covariance + self.measurement_noise)
        updated_state = predicted_state + kalman_gain * (measurement - predicted_state)
        updated_state_covariance = (np.eye(2) - kalman_gain) * predicted_state_covariance
        
        return updated_state,updated_state_covariance

    # TODO: wenn es keine Detektion gibt, sollte der prädizierte Wert zurückgegeben werden und nicht None
    def track(self, detection_result,dt,ptz):

        results = []
        if(detection_result.exists): 
            detectX = (detection_result.x2 + detection_result.x1) / 2
            detectY = (detection_result.y2 + detection_result.y1) / 2
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
            position = [] 
            print(ptz["pan"])
            print(ptz["zoom"])
            position.append(ptz["pan"]+Camera.get_delta_horizontal_degrees(results[0], ptz["zoom"]))
            position.append(ptz["tilt"]+Camera.get_delta_vertical_degrees(results[1], ptz["zoom"]))
            print(position)
            self.datei.write("\n"+':' + str(dt) + ': ' + str(position))
            return results


    