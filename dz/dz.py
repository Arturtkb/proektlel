import cv2
from PIL import Image
image_path = 'images-2023-03-03T165710.304.png'
image = cv2.imread(image_path)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
eye = eye_cascade.detectMultiScale(image)
smile = smile_cascade.detectMultiScale(image)
human = Image.open(image_path)
print(eye)
for (x, y, w, h) in eye:
    cv2.rectangle(image,(x,y), (x+w, y+h), (0, 255, 255), 3)

for (x, y, w, h) in smile:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

cv2.imshow("Humanayet and smile", image)
cv2.waitKey()