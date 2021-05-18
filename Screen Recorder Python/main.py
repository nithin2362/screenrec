import datetime

from PIL import ImageGrab,Image
import numpy as np
import cv2

width = 1920
height = 1080
time_stamp = datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')
rc = np.array(Image.open('recording.jpg'))
rc = cv2.cvtColor(rc,cv2.COLOR_BGR2RGB)
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
captured_video = cv2.VideoWriter(file_name, fourcc, 12.0, (width, height))
print('Press q to stop recording...')
print('Recording started')
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Status',rc)


    captured_video.write(img_final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captured_video.release()
cv2.destroyAllWindows()

print('Recording ended')