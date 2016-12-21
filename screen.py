# camera.py


import gtk
import time


class VideoCamera:
    def __init__(self, img_quality = 100):
        self.img_width = gtk.gdk.screen_width()
        self.img_height = gtk.gdk.screen_height()
        self.img_quality = img_quality
        self.img_buffer = ""
    def gtk_cb(self, buf):
        self.img_buffer += buf
        #print(buf)


    def get_frame(self):
        self.img_buffer = ""
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


            #print ("Done")
        except:
            print "Failed taking screenshot"
        screengrab.save_to_callback(self.gtk_cb, 'jpeg',  {"quality":str(self.img_quality)})
        return self.img_buffer

#Use for speed test
if __name__ == '__main__':
    n_frames = 100
    cam = VideoCamera(100)
    start = time.time()
    for i in range(0,n_frames):
        cam.get_frame()

    print("FPS: " + str( n_frames/(time.time() - start)))
