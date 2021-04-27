import cv2


cap = cv2.VideoCapture("testvideo.mp4")

fourcc = cv2.VideoWriter_fourcc(*"JPEG")

stream = cv2.VideoWriter('appsrc ! decodebin ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=10.42.0.1 port=5000',fourcc,25.0,(640,480))
while not stream.isOpened():
    stream = cv2.VideoWriter('appsrc ! decodebin ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=10.42.0.1 port=5000',fourcc,25.0,(640,480))
    print("yayın acıldı")
if cap.isOpened():
    print("video okundu")

while True:
    ret, frame = cap.read()
    stream.write(frame)

cap.release()
stream.release()
cv2.destroyAllWindows()
