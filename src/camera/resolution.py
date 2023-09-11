import math

def get_center_pixel(resolution):
    return (resolution[0]/2, resolution[1]/2)

def get_desired_diagonal_minlength(resolution):
    return math.sqrt((resolution[0]*(9/100))**2 +(resolution[1]*(9/100))**2 )

def get_desired_diagonal_maxlength(resolution):
    return math.sqrt((resolution[0]*(11/100))**2 +(resolution[1]*(11/100))**2 )

