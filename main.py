# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import numpy as np
prev_pos_list = []
red0 = np.array([0, 120, 70])
red1 = np.array([10, 255, 255])
green0 = np.array([36, 25, 25])
green1 = np.array([86, 255, 255])
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])
blue0 = np.array([110, 50, 50])
blue1 = np.array([130, 255, 255])
dist_prev = 0
scale=0
resize_ratio = 1

def detectColor (frame) :
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    redM = cv2.inRange(hsv, red0, red1)
    greenM = cv2.inRange(hsv, green0, green1)
    blueM = cv2.inRange(hsv, blue0, blue0)
    redR = cv2.bitwise_and(frame, frame, mask=redM)
    greenR = cv2.bitwise_and(frame, frame, mask=greenM)
    blueR = cv2.bitwise_and(frame, frame, mask=blueM)

    red(frame,redM)

    blue(frame)

    green(frame)
    return  redR,blueR,greenR

def red(frame,mask):
    ret, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    # Find contours in the threshold image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # If any contour is found, get its position and add it to the list of previous positions
    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 500:
            x, y, w, h = cv2.boundingRect(max_contour)
            prev_pos_list.append((x, y))
    # Draw lines between each pair of consecutive positions in the list
    for i in range(1, len(prev_pos_list)):
        cv2.line(frame, prev_pos_list[i - 1], prev_pos_list[i], (0, 0, 255), 2)

    return 0
def blue(frame):

    return 0

def green(frame):

    return 0
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    detectColor(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask using the lower and upper bounds of the green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours by area in descending order
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    # Draw a bounding box around the largest two contours with green color
    green_objects = []
    for i in range(2):
        if i < len(contours):
            (x, y, w, h) = cv2.boundingRect(contours[i])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Calculate the center of the bounding box
            center_x = x + w // 2
            center_y = y + h // 2

            # Save the center of the bounding box as a green object
            green_objects.append((center_x, center_y))

    # Calculate the distance between the two largest green objects
    if len(green_objects) == 2:
        (x1, y1), (x2, y2) = green_objects
        distance1 = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        cv2.putText(frame, f"Distance: {distance1:.2f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the frame

        scale = distance1
        scale=scale/1.5

        height, width, channels = frame.shape
        centerX, centerY = int(height / 2), int(width / 2)
        radiusX, radiusY = int(scale * height / 100), int(scale * width / 100)

        minX, maxX = centerX - radiusX, centerX + radiusX
        minY, maxY = centerY - radiusY, centerY + radiusY

        cropped = frame[minX:maxX, minY:maxY]
        frame = cv2.resize(cropped, (width, height))




    frame = cv2.flip(frame, 1)


    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask using the lower and upper bounds of the blue color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours by area in descending order
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    # Draw a bounding box around the largest two contours with blue color
    blue_objects = []
    for i in range(2):
        if i < len(contours):
            (x, y, w, h) = cv2.boundingRect(contours[i])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Calculate the center of the bounding box
            center_x = x + w // 2
            center_y = y + h // 2

            # Save the center of the bounding box as a blue object
            blue_objects.append((center_x, center_y))

    # Calculate the distance between the two largest blue objects
    if len(blue_objects) == 2:
        (x1, y1), (x2, y2) = blue_objects
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        cv2.putText(frame, f"Distance: {distance:.2f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Take a photo if the distance between the two largest blue objects is less than 100
        if distance < 120:

            cv2.imwrite('photo.png', frame)

    # Show the frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break


cap.release()
cv2.destroyAllWindows()
