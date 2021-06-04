import cv2
# pip install Pillow
from PIL import Image

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 30, 100)

    cv2.imshow('Video', img)
    cv2.imshow('Canny', canny)

    img.paste(canny, (0, 0))
    cv2.imshow('Video', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
