import pyautogui
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

green_low = np.array([36,25,25])
green_high = np.array([86, 255,255])
prev_y=0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv ,green_low, green_high)

    contours, hierarchy=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area=cv2.contourArea(c)
        if area>500:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y) ,(x+w, y+h), (0,255,0) ,2)

            if y < prev_y:
                print("down")
                pyautogui.press('down')

    cv2.imshow("d" ,frame)
    if cv2.waitKey(1) == 27:
        break;

cap.release()
cv2.destroyWindow()