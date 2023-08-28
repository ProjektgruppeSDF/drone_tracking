

query_videostream_flipped_ = "rtsp://192.168.11.103/axis-media/media.amp?videocodec=jpeg&resolution=800x450"
query_get_orientation = "http://192.168.11.103/axis-cgi/com/ptz.cgi?query=position)"


def get_query_continous_move(vx, vy):
    query = "http://192.168.11.103/axis-cgi/com/ptz.cgi?continuouspantiltmove="
    return query +str(vx)+','+str(vy)