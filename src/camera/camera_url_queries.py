

query_videostream_flipped_ = "rtsp://192.168.11.103/axis-media/media.amp?videocodec=jpeg&resolution=1920x1080"
query_get_orientation = "http://192.168.11.103/axis-cgi/com/ptz.cgi?query=position)"


def get_query_continous_move(vx, vy):
    query = "http://192.168.11.103/axis-cgi/com/ptz.cgi?continuouspantiltmove="
    return query +str(vx)+','+str(vy)

def get_query_absolute_pan(x):
    query = "http://192.168.11.103/axis-cgi/com/ptz.cgi?pan="
    return query +str(x)

def get_query_absolute_tilt(x):
    query = "http://192.168.11.103/axis-cgi/com/ptz.cgi?tilt="
    return query +str(x)

def get_query_zoom(x):
    query = "http://192.168.11.103/axis-cgi/com/ptz.cgi?zoom="
    return query +str(x)