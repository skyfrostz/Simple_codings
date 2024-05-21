# This code is used to read QR code from an image and display the QR code data.
import cv2
import numpy as np

# Read QR code image
img = cv2.imread('qrcode.png')

# initialize QR code detector
detector = cv2.QRCodeDetector()


# detect and decode
data, bbox, rectifiedImage = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(map(int, bbox[i][0]))
        point2 = tuple(map(int, bbox[(i+1) % n_lines][0]))
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()