import pyautogui
import time

# Move the mouse to the x, y coordinates
pyautogui.moveTo(100, 100, duration=1)  # Move to (100, 100) over 1 second

# Click the mouse at the current location
pyautogui.click()

# Move the mouse relative to its current position
pyautogui.moveRel(50, 50, duration=1)  # Move 50 pixels right and 50 pixels down

# Perform a right-click
pyautogui.rightClick()

# Perform a double-click
pyautogui.doubleClick()

# Drag the mouse to the x, y coordinates
pyautogui.dragTo(300, 300, duration=2)  # Drag to (300, 300) over 2 seconds

# Scroll the mouse up
pyautogui.scroll(100)  # Scroll up 100 units

# Scroll the mouse down
pyautogui.scroll(-100)  # Scroll down 100 units

# Get the current position of the mouse
current_mouse_x, current_mouse_y = pyautogui.position()
print(f"Current mouse position: ({current_mouse_x}, {current_mouse_y})")

# Pause between commands
pyautogui.PAUSE = 1  # Pause for 1 second after each command

# Display an alert box
pyautogui.alert('This is an alert box.')
