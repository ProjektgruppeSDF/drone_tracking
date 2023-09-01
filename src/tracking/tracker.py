
import numpy as np
from datetime import datetime
from datetime import timedelta

from camera.camera import Camera





class Tracker: 
    init_state = np.array([-1,-1,0,0])
    state_covariance = np.eye(4) * 1
    process_noise = np.eye(4) * 5 
    measurement_noise = np.eye(4) * 10 
    alt = init_state
    pdt = datetime.date
    state = init_state
    

    #def __init__(self) -> None:
        #self.datei = open('position.txt','a')

    def kalman_filter(self,measurement,tdems):
        measurement_funktion=np.matrix([[1,0,0,0],
                       [0,1,0,0]])
        dynamic = np.matrix([[1,0,tdems,0],
                       [0,1,0,tdems],
                       [0,0,1,0],
                       [0,0,0,1],])
        
        # Vorhersage 
        predicted_state = dynamic @ self.state
        predicted_state_covariance = dynamic @ self.state_covariance @ np.transpose(dynamic) + self.process_noise
        
        # Filterung
        sk = measurement_funktion @ predicted_state_covariance @ np.transpose(measurement_funktion) + self.measurement_noise
        wk = predicted_state_covariance @ np.transpose(measurement_funktion) @ np.linalg.inv(sk)
        vk = measurement - measurement_funktion @ predicted_state
        self.state = predicted_state + wk @ vk
        self.state_covariance = predicted_state_covariance - wk @ sk @ np.transpose(wk)



    # TODO: wenn es keine Detektion gibt, sollte der prädizierte Wert zurückgegeben werden und nicht None
    
    def track(self, detection_result,dt):

        results = []
        detectX = (detection_result.x2 + detection_result.x1) / 2
        detectY = (detection_result.y2 + detection_result.y1) / 2
        measurement = np.array([detectX,detectY])
        if(np.array_equal(self.state, self.init_state)):
                #initalisierung
            self.state[0] = measurement[0]
            self.state[1]= measurement[1]
            self.alt = self.state
            self.pdt = dt
        else:
            tde = self.pdt - dt
            tdems = int(tde/timedelta(milliseconds=1))
            self.kalman_filter(measurement,tdems)

            self.state[2] = (self.state[0]-self.alt[0])/ tdems
            self.state[3] = (self.state[1]-self.alt[1])/ tdems
            self.alt = self.state

        results.append(self.state[0])
        results.append(self.state[1])
        return results
    

    def reinitialise(self):
        self.state = self.init_state

