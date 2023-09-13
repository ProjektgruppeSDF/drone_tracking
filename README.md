This program controls a ptz-network-camera of model Axis-M5525 such that the camera image automatically follows a person or a flying drone. It uses either YOLOv8 or RT-DETR to detect, a kalman filter
as tracking algorithm and the VAPIX-API to control the camera movement.

For drone detection, ULtralytics YOLOv8 and RT-DETR were trained on a custom created (and annotated) drone dataset. Images were either downloaded from other publicly availlable drone datasets or
captured by us. The images and annotations can be downloaded in the link below. The obtained weights are stored in the resources folder.

https://www.dropbox.com/sh/4uc76f7wkfismth/AAAF3n8RATF9KYvuUhkS_cufa?dl=0


This program was created as part of a university project at the University of Bonn. Translate german comments to english (with ChatGPT) if needed.

