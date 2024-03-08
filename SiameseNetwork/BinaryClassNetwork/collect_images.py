
import cv2
import numpy
import os
import uuid


BASE = os.path.join('data', 'base')
COR = os.path.join('data', 'positive')
INCOR = os.path.join('data', 'negative')

# set the size of the frame
# 500, 281



cam = cv2.VideoCapture(0)

cv2.namedWindow("test")



while True:
    ret, frame = cam.read()

     # display the size of the frame
    #print(frame.shape) (720, 1280, 3) So now i know that I need to maintain a aspect ratio of 16:9 in order to avoid too muchd distortion

    frame = cv2.resize(frame, (720, 400))
    # cut the frame into a 250x250 square (since our images in the dataset are 250x250)
    frame = frame[120:120+250,200:200+250, :]
    # zoom out on the frame

   

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("Collect Images", frame)

    
    # cut frame to be in the center

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = os.path.join(BASE, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(img_name, frame)

    elif k%256 == 13:
        # ENTER pressed
        img_name = os.path.join(COR, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(img_name, frame)

cam.release()

cv2.destroyAllWindows()

"""
NOTES: 

Image Dimensions for Reference
https://aspectratiocalculator.com/16-9.html

___________________________________________________________________

Image Type                   |     Dimensions      |  Aspect Ratio
___________________________________________________________________

Background Image 	         |   1920 x 1080 px    |	 16:9
Hero Image          	     |   1280 x 720 px 	   |     16:9
Website Banner      	     |    250 x 250 px 	   |      1:1
Blog Image 	                 |   1200 x 630 px 	   |      3:2
Logo (Rectangle)             |    250 x 100 px 	   |      2:3
Logo (Square) 	             |    100 x 100 px     |      1:1
Favicon 	                 |     16 x 16 px      |      1:1
Social Media Icons           |	  32 x 32 px 	   |      1:1
Lightbox Images (Full Screen)| 	1600 x 500 px 	   |     16:9
Thumbnail Image 	         |    150 x 150 px 	   |      1:1



"""