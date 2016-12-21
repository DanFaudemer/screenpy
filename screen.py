# camera.py

import cv2
import numpy
import gtk, Image
import time


class VideoCamera:
    def __init__(self):
        self.img_width = gtk.gdk.screen_width()
        self.img_height = gtk.gdk.screen_height()

    def get_frame(self):
        try:
            screengrab = gtk.gdk.Pixbuf(
            gtk.gdk.COLORSPACE_RGB,
            False,
            8,
            self.img_width,
            self.img_height
            )

            screengrab.get_from_drawable(
            gtk.gdk.get_default_root_window(),
            gtk.gdk.colormap_get_system(),
            0, 0, 0, 0,
            self.img_width,
            self.img_height
            )

        except:
            print "Failed taking screenshot"

        #print "Converting to PIL image ..."
        final_screengrab = Image.frombuffer(
        "RGB",
        (self.img_width, self.img_height),
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


#Use for speed test
if __name__ == '__main__':
    n_frames = 100
    cam = VideoCamera()
    start = time.time()
    for i in range(0,n_frames):
        cam.get_frame()

    print("FPS: " + str( n_frames/(time.time() - start)))
