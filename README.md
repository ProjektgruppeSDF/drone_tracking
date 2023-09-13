This program controls a ptz-network-camera of model Axis-M5525 such that the camera image automatically follows a person or a flying drone. It uses either YOLOv8 or RT-DETR to detect, a kalman filter as tracking algorithm and the VAPIX-API to control the camera movement.

This program incorporates a scan mode to search for targets and a tracking mode to follow them. Additionally, the camera will zoom until a sufficient box size is reached. We used a computer with a Intel i9 and a 2080 Ti und 1050 Ti. While this program was mostly intended as practice and a proof of concept, we successfully achieved real-time-tracking at moderate distances with a FPS-rate of about 10. 

For drone detection, ULtralytics YOLOv8 and RT-DETR were trained on a custom created (and annotated) drone dataset. Images were either downloaded from other publicly availlable drone datasets or
captured by us. The images and annotations can be downloaded in the link below. The obtained weights are stored in the resources folder.

https://www.dropbox.com/sh/4uc76f7wkfismth/AAAF3n8RATF9KYvuUhkS_cufa?dl=0


This program was created as part of a university project at the University of Bonn. Translate german comments to english (with ChatGPT) if needed. A more detailed description is found in the project report "Projektbericht" folder (in german). Please view the activity diagram in the report to get a basic understanding of the program flow.

