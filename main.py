import cv2
from detect import *

tracker = EuDistTracker()

frames = cv2.VideoCapture("highway2.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = frames.read()
    height, width, _ = frame.shape #(height, width, channels)

    roi = frame[340: 720,200: 1000]
    #roi = frame[340: 720,500: 800]
    #roi = frame[394: 600,271: 663]
    
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY) #cv2.THRESH_BINARY_INV
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #(image,mode,contour compression method simple-only 4lines for rectangle)
    detections = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > 100:
            #cv2.drawContours(roi, [i], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(i)
            detections.append([x, y, w, h])

    
    boxes_ids = tracker.update(detections)
    for i in boxes_ids:
        x, y, w, h, id = i
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("ROI", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30) 
    if key == 27:
        break
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

frames.release()
cv2.destroyAllWindows()

