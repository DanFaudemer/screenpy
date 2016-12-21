# camera.py

import cv2

import pyscreenshot as ImageGrab

import numpy
import gtk, Image

class VideoCamera:
    def __init__(self):
        self.init = "toto"
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):


        try:

            img_width = gtk.gdk.screen_width()
            img_height = gtk.gdk.screen_height()

            screengrab = gtk.gdk.Pixbuf(
            gtk.gdk.COLORSPACE_RGB,
            False,
            8,
            img_width,
            img_height
            )

            screengrab.get_from_drawable(
            gtk.gdk.get_default_root_window(),
            gtk.gdk.colormap_get_system(),
            0, 0, 0, 0,
            img_width,
            img_height
            )

        except:
            print "Failed taking screenshot"
            exit()

        #print "Converting to PIL image ..."
        final_screengrab = Image.frombuffer(
        "RGB",
        (img_width, img_height),
        screengrab.get_pixels(),
        "raw",
        "RGB",
        screengrab.get_rowstride(),
        1
        )

        image = numpy.array(final_screengrab.convert('RGB'))
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()



if __name__ == '__main__':

    cam = VideoCamera()
    #print "Ok"
    for i in range(0,100):
        cam.get_frame()
        #print i
