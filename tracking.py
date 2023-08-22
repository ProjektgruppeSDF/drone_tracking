import cv2

# RTSP-Stream URL
rtsp_url = 'DEINE_RTSP_STREAM_URL'

# Videoaufnahme starten
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Fehler beim Öffnen des RTSP-Streams.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("RTSP-Stream beendet.")
        break
    
    cv2.imshow('RTSP Stream', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()