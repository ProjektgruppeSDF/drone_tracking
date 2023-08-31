from config.global_config import *

query_videostream_flipped_ = "rtsp://{}/axis-media/media.amp?videocodec=jpeg&resolution={}x{}&fps={}&rotation=180".format(camera_ip, camera_resolution[0], camera_resolution[1], camera_fps)
query_get_orientation = "http://{}/axis-cgi/com/ptz.cgi?query=position)".format(camera_ip)


def get_query_continous_move(vx, vy):
    query = "http://{}/axis-cgi/com/ptz.cgi?continuouspantiltmove=".format(camera_ip)
    return query +str(vx)+','+str(vy)

def get_query_absolute_pan(x):
    query = "http://{}/axis-cgi/com/ptz.cgi?pan=".format(camera_ip)
    return query +str(x)

def get_query_absolute_tilt(x):
    query = "http://{}/axis-cgi/com/ptz.cgi?tilt=".format(camera_ip)
    return query +str(x)

def get_query_zoom(x):
    query = "http://{}/axis-cgi/com/ptz.cgi?zoom=".format(camera_ip)
    return query +str(x)