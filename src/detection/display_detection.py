import cv2
from datetime import datetime

def display_image_with_detection(image, detectionBox,target_loss_monitorer):
    image = draw_detection_on_image(image, detectionBox)
    displayImage(image,"Tracking Modus",target_loss_monitorer)
        

    

def draw_detection_on_image(image, detectionBox):

    if(detectionBox.exists):
        cv2.rectangle(image, (detectionBox.x1, detectionBox.y1), (detectionBox.x2, detectionBox.y2), (255, 0, 255), 3)

        org = [detectionBox.x1, detectionBox.y2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        label = "Class: " + detectionBox.class_label + ", Confidence: " + str(detectionBox.confidence)


        cv2.putText(image, label, org, font, fontScale, color, thickness)

    return image

def displayImage(image,modus, target_loss_monitorer):
    org = [0,1080]
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 0, 255)
    thickness = 2
    label = modus
    cv2.putText(image, label, org, font, fontScale, color, thickness)

    displayTime(image, target_loss_monitorer.get_time_last_detection())

    cv2.imshow('Video', image)
    cv2.waitKey(1)

def displayTime(image,last_detected_time):
    org = [0, 25]
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 0, 255)
    thickness = 2
    label = str(datetime.now())

    cv2.putText(image, label, org, font, fontScale, color, thickness)
    org = [0, 50]
    label = str(last_detected_time)

    cv2.putText(image, label, org, font, fontScale, color, thickness)