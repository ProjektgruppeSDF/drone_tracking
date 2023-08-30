import signal
import sys
from camera.camera import Camera

def signal_handler(sig, frame):
    Camera.move_to_default_position()
    sys.exit(0)

def set_exit_strategy():
    signal.signal(signal.SIGINT, signal_handler)


