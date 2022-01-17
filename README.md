# Raspberry PI Smart Safe through Face Recognition
Last Updated: 17 Jan 2022

Hi! As a student curious about the usage of IOT and the interaction
between Robotic Hardware and Software, I thought of diving into my own personal 
project of creating a Facial Recognition programme with a Raspberry Pi. 

As a motivating idea for a Facial Recognition Programme, I thought of creating a Smart Safe
using a RPI, a RPI Camera and a Servo. 

The camera will detect a frame and try to recognise the face based on pretrained embeddings. 
If a face is recognised, the servo will rotate to unlock a box.

As this is my first time playing around with a RPI, I'm quite careless with the required hardware 
materials like jumper wire, RPI charger and stuff so the actual construction of the hardware still needs some time due to the lack of materials

However, I created the code with some reference to online materials like https://core-electronics.com.au/tutorials/face-identify-raspberry-pi.html and https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/ while I tweaked the code to fit my own purpose.

The current programme was set up quite easily due to the usage of the face_recognition package on Python which employs the use of dlib. 

I'm a total newbie to the world of raspberry pi and hardware like circuit boards so my intended process for building this project is an iterative one, where I improve slowly by redesigning sections of the project instead of going directly for a huge project which entails things like training my own model and improving the FPS of the cameras by centroid tracking etc. 

I will be documenting my progress along the way for memory sake and hopefully it can help to boost my portfolio by giving a glimspe of my interest in robotics as a Computer Science undergrad :D 

Thanks!