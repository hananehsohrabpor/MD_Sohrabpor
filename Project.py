import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def get_frame_gray (cap):
    ret, frame = cap.read()
    frame = frame[:,130:550]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    return frame,gray
while True:
    frame,gray = get_frame_gray(cap)
    cv2.imshow('farme',frame)
    cv2.imshow('gray blur',gray)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
