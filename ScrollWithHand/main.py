#importing libraries
import cv2
#record the hand
import mediapipe as mp
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
#capture the video
cap = cv2.VideoCapture(0)

while True: 
    _, frame = cap.read()
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgbFrame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
    print(hands)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)