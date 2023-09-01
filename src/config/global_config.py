import os


camera_ip = "192.168.11.103"
camera_resolution = (1920,1080)
camera_fps = 11

def disable_proxy_server_for_camera():
    os.environ["NO_PROXY"] = camera_ip