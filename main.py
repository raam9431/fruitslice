import mediapipe as mp
import cv2
import numpy as pm
from mediapipe.framework.formats import landmark_pb2
import time
import win32api
import pyautogui
 
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5) as hands:
    while video.isOpened():
        _,frame = video.read()
        image = cv2.cvtColor(frame,cv2,COLOR_BGR2RGB)
        image = cv2.flip(image,1)

        image_height,image_widht,_ = image.shape

        results = hands.process(image)

        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        if results.multi_hands_landmark:
            for num,hand in enumerate(results.multi_hands_landmarks):
                mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color = (250,44,250),thickness = 2,circle_radius = 2))

        if results.multi_hands_landmark !=None:
            for handsLandmarks in results.multi_hands_landmarks:
                for points in mp_hands.HandLandmark:
                    normalizedLandmark = handsLandmarks.landmark[points]
                    pixelCoordinatesLandmark = mp_drawing.normalized_to_pixel_cordinates(normalizedLandmark.x,normalizedLandmark.y,image_widht,image_height)
                    if points == 'HandLandmark.INDEX_FIGHTER_TIP':
                        try:
                            cv2.circle(image,pixelCoordinatesLandmark[0],pixelCoordinatesLandmark[1],25,(0,200,0),5)
                            indexfingertip_x = pixelCoordinatesLandmark[0]
                            indexfingertip_y = pixelCoordinatesLandmark[1]
                            win32api.SetCursorPos((indexfingertip_x*4),indexfingertip_y*5)
                            pyautogui.mouseDown(button = 'left')

                        except:
                            pass

    cv2.imshow('game',image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
    break

video.release()
cv2.destroyAllWindows()
