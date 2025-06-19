import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

dragging = False  # To keep track of drag state
pinch_start_time = None  # To measure pinch duration

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror the frame

    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            # Finger positions
            thumb_x = thumb_y = 0
            index_x = index_y = 0
            middle_x = middle_y = 0
            index_base_x = index_base_y = 0
            ring_tip_x = ring_tip_y = 0
            ring_base_x = ring_base_y = 0

            for id, lm in enumerate(landmarks):
                x = int(lm.x * frame_width)
                y = int(lm.y * frame_height)

                if id == 4:  # Thumb Tip (Yellow)
                    cv2.circle(frame, (x, y), 8, (0, 255, 255), -1)
                    thumb_x = (screen_width / frame_width) * x
                    thumb_y = (screen_height / frame_height) * y
                elif id == 5:  # Index Base
                    cv2.circle(frame, (x, y), 8, (255, 127, 148), -1)
                    index_base_x = (screen_width / frame_width) * x
                    index_base_y = (screen_height / frame_height) * y
                elif id == 8:  # Index Tip (Green)
                    cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)
                    index_x = (screen_width / frame_width) * x
                    index_y = (screen_height / frame_height) * y
                elif id == 12:  # Middle Tip (Blue)
                    cv2.circle(frame, (x, y), 8, (255, 0, 0), -1)
                    middle_x = (screen_width / frame_width) * x
                    middle_y = (screen_height / frame_height) * y
                elif id == 16:  # Ring Tip (Orange)
                    cv2.circle(frame, (x, y), 8, (0, 165, 255), -1)
                    ring_tip_x = (screen_width / frame_width) * x
                    ring_tip_y = (screen_height / frame_height) * y
                elif id == 13:  # Ring Base (Purple)
                    cv2.circle(frame, (x, y), 8, (128, 0, 128), -1)
                    ring_base_x = (screen_width / frame_width) * x
                    ring_base_y = (screen_height / frame_height) * y
                # Pinky detection REMOVED as requested (ID 20)

            # Move mouse pointer with Index Finger Tip (instead of Thumb)
            pyautogui.moveTo(index_x, index_y)

            # --- Left Click: Thumb tip close to Index tip ---
            if abs(thumb_x - index_x) < 40 and abs(thumb_y - index_y) < 40:
                pyautogui.click()
                pyautogui.sleep(1)

            # --- Right Click: Thumb tip close to Middle tip ---
            elif abs(thumb_x - middle_x) < 40 and abs(thumb_y - middle_y) < 40:
                pyautogui.rightClick()
                pyautogui.sleep(1)

            # --- Scroll Down: Thumb tip close to Ring base ---
            elif abs(thumb_x - ring_base_x) < 40 and abs(thumb_y - ring_base_y) < 40:
                pyautogui.scroll(-500)
                pyautogui.sleep(1)

            # --- Scroll Up: Thumb tip close to Ring tip ---
            elif abs(thumb_x - ring_tip_x) < 40 and abs(thumb_y - ring_tip_y) < 40:
                pyautogui.scroll(500)
                pyautogui.sleep(1)

            # --- Drag Start/Stop: Thumb Tip close to Index Base for 2 sec ---
            pinch_distance = max(abs(thumb_x - index_base_x), abs(thumb_y - index_base_y))

            if pinch_distance < 30:  # Sensitivity threshold
                if pinch_start_time is None:
                    pinch_start_time = time.time()
                elif time.time() - pinch_start_time >= 2 and not dragging:
                    pyautogui.mouseDown()  # Start drag after 2 seconds
                    dragging = True
                    print("Drag Started")
            else:
                pinch_start_time = None
                if dragging:
                    pyautogui.mouseUp()  # Release drag when fingers apart
                    dragging = False
                    print("Drag Stopped")

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
