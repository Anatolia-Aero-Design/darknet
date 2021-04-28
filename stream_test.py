import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*"X264")
cap = cv2.VideoCapture("testvideo.mp4")
#RECİEVE="gst-launch-1.0 -v udpsrc port=5000 caps = 'application/x-rtp, media=(string)video, encoding-name=(string)H264, payload=(int)26' ! rtph264depay ! decodebin ! videoconvert ! xvimagesink"
pipe = "appsrc ! videoconvert ! videoscale ! x264enc tune=zerolatency ! rtph264pay config-interval=0 ! udpsink host=10.42.0.1 port=5000 sync=1"
calışıyor = "appsrc ! videoconvert ! videoscale ! video/x-raw,format=xBGR, width=480,height=640 !  videoconvert ! videoscale ! x264enc bitrate=90000 ! rtph264pay ! udpsink host=10.42.0.1 port=5000 sync=false"
stream = cv2.VideoWriter(pipe,fourcc,30.0,(640,480), True)
while stream.isOpened():
    _, frame = cap.read()
    print("deneme")
    print(frame.shape)
    
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    stream.write(frame)



stream.release()

