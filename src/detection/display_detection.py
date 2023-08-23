import cv2

def display_image_with_detection(image, detectionBoxes,video):
    image = draw_detection_on_image(image, detectionBoxes)
    displayImage(image,video)
        

    

def draw_detection_on_image(image, detectionBoxes):
    for detectionBox in detectionBoxes:
        if detectionBox.class_label == "person":
            cv2.rectangle(image, (detectionBox.x1, detectionBox.y1), (detectionBox.x2, detectionBox.y2), (255, 0, 255), 3)

            org = [detectionBox.x1, detectionBox.y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(image, detectionBox.class_label, org, font, fontScale, color, thickness)

    return image

def displayImage(image,video):
    cv2.imshow('Webcam', image)
    video.write(image)
    cv2.waitKey(1)