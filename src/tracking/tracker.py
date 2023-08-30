
import numpy as np
from datetime import datetime
from datetime import timedelta

from camera.camera import Camera





class Tracker: 
    init_state = np.array([-1,-1])
    state_covariance = np.eye(2) * 1
    process_noise = np.eye(2) * 5  
    measurement_noise = np.eye(2) * 1 
    velocity = np.array([0,0]) 
    alt = np.array([-1,-1])
    pdt = datetime.date
    state = init_state
    

    def __init__(self) -> None:
        self.datei = open('position.txt','a')

    def kalman_filter(self,measurement,tdems):
        
        # Vorhersage 
        self.velocity[0] = self.velocity[0]*tdems
        self.velocity[1] = self.velocity[1]*tdems
        predicted_state = self.state + self.velocity
        predicted_state_covariance = self.state_covariance + self.process_noise
        
        # Filterung
        kalman_gain = np.dot(predicted_state_covariance,np.linalg.inv(predicted_state_covariance + self.measurement_noise))
        self.state+= np.dot(kalman_gain,(measurement - predicted_state))
        self.state_covariance = (np.eye(2) - kalman_gain) * predicted_state_covariance


    # TODO: wenn es keine Detektion gibt, sollte der prädizierte Wert zurückgegeben werden und nicht None
    
    def track(self, detection_result,dt):

        results = []
        detectX = (detection_result.x2 + detection_result.x1) / 2
        detectY = (detection_result.y2 + detection_result.y1) / 2
        measurement = np.array([detectX,detectY])
        if(np.array_equal(self.state, self.init_state)):
                #initalisierung
            self.state = measurement
            self.velocity = [0,0]
            self.alt = measurement
            self.pdt = dt
        else:
            tde = self.pdt - dt
            tdems = int(tde/timedelta(milliseconds=1))
            self.kalman_filter(measurement,tdems)

            self.velocity = (self.state-self.alt) /tdems
            self.alt = self.state

        results.append(self.state[0])
        results.append(self.state[1])
        return results
    

    def reinitialise(self):
        self.state = self.init_state

    