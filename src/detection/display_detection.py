import cv2

def display_image_with_detection(image, detectionBox):
    image = draw_detection_on_image(image, detectionBox)
    displayImage(image,"Tracking Modus")
        

    

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

def displayImage(image,modus):
    org = [0,1080]
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 0, 255)
    thickness = 2
    label = modus


    cv2.putText(image, label, org, font, fontScale, color, thickness)
    cv2.imshow('Video', image)
    cv2.waitKey(1)