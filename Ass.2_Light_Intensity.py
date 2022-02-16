# ####EEGR 675 Homework 2#######
# Lab goal is to access camera and get familiar with open commands and simple calculations
# of video properties

###Import necessary libraries
import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
###Create a 20 element list initialized to 150 on start
ave_intvec = [150] * 20

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_COMPLEX
    color = (0, 255, 0) ### Color is in BGR and GR gives yellow

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    av_int = np.average(gray_frame)
    homeworknametxt="EEGR 675: Homework 2"
    next_txt= "Ave light Intensity = "+str(round(av_int,2))
    gray_frame= cv2.putText(gray_frame,homeworknametxt ,(25,25),font,0.5,color,1,cv2.LINE_AA)
    gray_frame = cv2.putText(gray_frame, next_txt, (25, 50), font, 0.5, color, 1, cv2.LINE_AA)





    frame= cv2.putText(frame,homeworknametxt ,(25,25),font,0.5,color,1,cv2.LINE_AA)

    frame = cv2.putText(frame, next_txt, (25, 50), font, 0.5, color, 1, cv2.LINE_AA)

    # load new intensity values from the right and remove left values...left shift in
    ave_intvec.append(av_int)
    ave_intvec.pop(0)

    if np.all(np.array(ave_intvec)<100): ### Only come on when all intensities over 20 loops are > 100
        Light_stat= "Light On"
    else:
        Light_stat= "Light off"

    frame = cv2.putText(frame, Light_stat, (300, 50), font, 0.5, (255, 255, 0), 1, cv2.LINE_AA)

    # Display the resulting frame

    cv2.imshow('Deji_cam1',frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()