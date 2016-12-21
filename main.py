# main.py

from flask import Flask, render_template, Response, request
from screen import VideoCamera
from pymouse import PyMouse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera(100)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/move', methods=['POST'])
def move():
    posx=int(request.form['posx'])
    posy=int(request.form['posy'])
    m.move(posx,posy)
    return "success"


if __name__ == '__main__':
    m = PyMouse()
    app.run(host='0.0.0.0')
