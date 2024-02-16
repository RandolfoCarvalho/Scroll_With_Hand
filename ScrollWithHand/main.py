#importing libraries
import cv2
#record the hand
import mediapipe as mp
#mouse manipulation
import pyautogui

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height, = pyautogui.size()
index_y = 0
#capture the video
cap = cv2.VideoCapture(0)

while True: 
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgbFrame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmarks in enumerate(landmarks):
                x = int(landmarks.x * frame_width)
                y = int(landmarks.y * frame_height)
                if id == 8:
                    cv2.circle(img = frame, center=(x, y), radius=15, color=(0, 255, 255))
                    index_x = screen_width/frame_width * x
                    index_y = screen_height/frame_height * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img = frame, center=(x, y), radius=15, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width * x
                    thumb_y = screen_height/frame_height * y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 90:
                        pyautogui.click()
                        pyautogui.sleep(1)


    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)