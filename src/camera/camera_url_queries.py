

query_videostream_flipped_ = "rtsp://192.168.11.103/axis-media/media.amp?videocodec=jpeg&resolution=800x450&rotation180"
query_get_orientation = "http://192.168.11.103/axis-cgi/com/ptz.cgi?query=position)"


def get_query_continous_move(delta_x, delta_y):
    query = "http://192.168.11.103/axis-cgi/com/ptz.cgi?continuouspantiltmove="
    return query +str(int(delta_x))+','+str(int(delta_y))