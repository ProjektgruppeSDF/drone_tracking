import cv2

def display_image_with_detection(image, detectionBox):
    image = draw_detection_on_image(image, detectionBox)
    displayImage(image)
        

    

def draw_detection_on_image(image, detectionBox):

    if(detectionBox.exists):
        cv2.rectangle(image, (detectionBox.x1, detectionBox.y1), (detectionBox.x2, detectionBox.y2), (255, 0, 255), 3)

        org = [detectionBox.x1, detectionBox.y1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2

        cv2.putText(image, detectionBox.class_label, org, font, fontScale, color, thickness)

    return image

def displayImage(image):
    cv2.imshow('Webcam', image)
    cv2.waitKey(1)