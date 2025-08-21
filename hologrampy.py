import cv2
import mediapipe as mp
import numpy as np
import time


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()


images = [cv2.imread("ball.jpg"), cv2.imread("Batman.jpg"), cv2.imread("superman.jpg"), cv2.imread("messsi.jpg"), cv2.imread("ronaldo.jpg"), cv2.imread("neymar.jpg")]
if any(img is None for img in images):
    print("Error loading one or more images!")
    exit()
current_image_index = 0  


last_swipe_time = 0
swipe_delay = 2  

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            fingers_up = []
            finger_tips = [
                mp_hands.HandLandmark.INDEX_FINGER_TIP,
                mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            ]
            for tip in finger_tips:
                
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                    fingers_up.append(tip)

            current_time = time.time()

            
            if (current_time - last_swipe_time) > swipe_delay:
                if len(fingers_up) == 1: 
                    current_image_index = (current_image_index + 1) % len(images)
                    print("One finger detected, swiping right to next image")
                    last_swipe_time = current_time

                elif len(fingers_up) == 2:  
                    current_image_index = (current_image_index - 1) % len(images)
                    print("Two fingers detected, swiping left to previous image")
                    last_swipe_time = current_time

    
    img = images[current_image_index]
    img_height, img_width = img.shape[:2]
    resized_img = cv2.resize(img, (frame.shape[1], frame.shape[0]))
    frame = resized_img.copy()

    cv2.imshow("Hologram Image Slider", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
