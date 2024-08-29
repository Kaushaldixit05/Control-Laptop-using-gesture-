import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Open webcam
cap = cv2.VideoCapture(0)

# Set capture frame dimensions to match screen dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, screen_height)

# Define a smoothing factor
smooth_factor = 0.5

# Initialize previous thumb position
prev_tx, prev_ty = 0, 0

# Initialize previous index finger and thumb distance
prev_distance = 0

# Flag to track mouse click state
mouse_clicked = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)
    
    # Convert BGR image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract hand landmarks
            landmarks = np.array([[lm.x, lm.y] for lm in hand_landmarks.landmark])
            
            # Get the coordinates of index finger and thumb
            index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb = landmarks[mp_hands.HandLandmark.THUMB_TIP]
            
            # Convert thumb coordinates to screen dimensions
            tx = int(thumb[0] * screen_width)
            ty = int(thumb[1] * screen_height)
            
            # Smooth cursor movement
            tx = smooth_factor * prev_tx + (1 - smooth_factor) * tx
            ty = smooth_factor * prev_ty + (1 - smooth_factor) * ty
            
            # Move cursor based on thumb movement
            pyautogui.moveTo(tx, ty)
            
            # Update previous thumb position
            prev_tx, prev_ty = tx, ty
            
            # Calculate distance between index finger and thumb
            distance = np.sqrt((index_finger[0] - thumb[0])**2 + (index_finger[1] - thumb[1])**2)
            
            # Check for mouse click gesture
            if prev_distance - distance > 0.02:  # Threshold for finger-thumb distance change
                if not mouse_clicked:
                    pyautogui.mouseDown()  # Press mouse button down
                    mouse_clicked = True
            else:
                if mouse_clicked:
                    pyautogui.mouseUp()  # Release mouse button
                    mouse_clicked = False
            
            # Update previous index finger and thumb distance
            prev_distance = distance
            
            # Add a small delay
            time.sleep(0.01)
    
    # Display the frame
    cv2.imshow('Hand Gesture Control', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
