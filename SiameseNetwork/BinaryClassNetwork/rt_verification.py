import cv2
import numpy as np
import os
import uuid
import tensorflow as tf
from verification import verify
import pandas as pd


cam = cv2.VideoCapture(1)

cv2.namedWindow("Verify")

while True:
    ret, frame = cam.read()


    frame = cv2.resize(frame, (720, 400))
    # cut the frame into a 250x250 square (since our images in the dataset are 250x250)
    frame = frame[120:120+250,200:200+250, :]
    # zoom out on the frame

    

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("Verify", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break


    # key = v 
    elif k%256 == 118:
        # v pressed
        img_name = os.path.join('application', 'input', 'to_verify.jpg')
        cv2.imwrite(img_name, frame)
        print("Image saved to {}".format(img_name))
        #results, verified = verify(model, 0.5, 0.5)


cam.release()
cv2.destroyAllWindows()

