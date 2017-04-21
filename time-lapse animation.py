from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (1280, 720)

for i in range(30):
  camera.rotation = 270
  sleep(60)
  camera.capture('/home/pi/Desktop/timelapse/image{0:04d}.jpg'.format(i))
system('convert -delay 40 -loop 0 /home/pi/Desktop/timelapse/image*.jpg /home/pi/Desktop/timelapse/animation.gif')
print('done')
