import cv2
import time
from picamera2 import Picamera2

picam = Picamera2()
picam.preview_configuration.main.size = (1280,720)
picam.preview_configuration.main.format = "RGB888"
picam.preview_configuration.align()
picam.configure("preview")
picam.start()
currTime = time.time()
prevTime = None
while True:
    prevTime = currTime
    currTime = time.time()
    fps = 1.00/(currTime - prevTime)

    im = picam.capture_array()
    im = cv2.putText(im, f'FPS: {fps}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Camera", im)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()