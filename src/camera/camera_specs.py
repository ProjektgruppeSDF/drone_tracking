import numpy as np

image_dimension = (1920, 1080)
fov_angle_horizontal_min_zoom = 61.8
fov_angle_vertical_min_zoom =  37.2
fov_angle_horizontal_max_zoom = 6.7
fov_angle_vertical_max_zoom =  3.8
min_zoom = 1
max_zoom = 9999

zoom_measurements = np.array([1,25,50,75,100,200,300,400,500,750,1000,1500,2000,3000,4000,5000,7500,9500])
fov_measurements = np.array([61.816,60.563,59.066,58.198, 56.852, 53.013, 49.522, 46.455, 43.604, 38.626, 34.121, 28.405, 24.435, 18.522, 15.152, 12.948, 8.941, 7.210])

# Es wird angenommen, dass sich die Abhängigkeit des vertikalen fov von der Zoomstufe nicht anders verhält als die horizontale Abhängigkeit
def get_fov_horizontal(zoom):
    
    lowest_deviance = np.inf
    lowest_deviance_index = 0

    for i in range(len(zoom_measurements)):
        if np.abs(zoom_measurements[i]-zoom) < lowest_deviance:
            lowest_deviance_index = i

    return fov_measurements[lowest_deviance_index]


def get_fov_ratio_factor(zoom):
    fov = get_fov_horizontal(zoom)
    fov_at_no_zoom = 61.816
    return fov/fov_at_no_zoom


