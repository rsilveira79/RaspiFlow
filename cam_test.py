import time
import picamera
import picamera.array
import cv2
import io
from fractions import Fraction

def main():
#    camera=PiCamera()
#    camera.resolution=(1280,720)
#    camera.exif_tags['IFD0.Artist'] = 'Beto'
    
    '''
    with picamera.PiCamera() as camera:
        try:
            camera.start_preview()
            camera.led = False
            for i in range(10):
                camera.capture("./images/foobar{}.jpg".format(i))
                camera.annotate_text = 'Hello world {}!'.format(i)
                time.sleep(1)
        finally:
            camera.stop_preview()
    '''
    '''
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as stream:
            camera.resolution= (1024,768)
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream,'rgb')
            
            print(stream.array.shape)
    '''
    '''
    with picamera.PiCamera() as camera:
        camera.framerate = Fraction(1,6)
        camera.shutter_speed = 6000000
        camera.exposure_mode = 'off'
        camera.iso = 800
        time.sleep(5)
        camera.start_preview()
        for i in range(5):
            camera.capture('./images/dark{}.jpg'.format(i))
            time.sleep(0.5)
        camera.stop_preview()
    '''
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.framerate = 30
        camera.start_preview()
        time.sleep(2)
        start = time.time()
        camera.capture_sequence([
            './images/img1.jpg',
            './images/img2.jpg',
            './images/img3.jpg',
            './images/img4.jpg',
            './images/img5.jpg'])
        camera.stop_preview()
        finish = time.time()
        print('Captured 5 frames in {} seconds'.format(finish-start))
if __name__ == '__main__':
    main()
