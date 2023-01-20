import cv2
import numpy
from flask import Flask, render_template, Response, stream_with_context, request

video = cv2.VideoCapture(0)


app = Flask('__name__')

# def video_stream():
#     # Create a video writer object
#     fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#     out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

#     while True:
#         ret, frame = video.read()
#         if not ret:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpeg', frame)
#             frame = buffer.tobytes()

#             # Write the frame to the video file
#             out.write(frame)

#             yield (b' --frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#     # Release the video writer object
#     out.release()

def video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpeg', frame)
            frame= buffer.tobytes()
            yield (b' --frame\r\n' b'Content-type: image/jpeg\r\n\r\n' + frame +b'\r\n')


@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=False)