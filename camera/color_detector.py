# -*- coding: utf-8 -*-

import time
import RPi.GPIO as g
import cv2

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=480,
    display_height=270,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def main():
    
    g.setwarnings(False)
    g.setmode(g.BCM)
    

    gstream = gstreamer_pipeline(flip_method=2)
    
    print(gstream)
    cam = cv2.VideoCapture(gstream, cv2.CAP_GSTREAMER)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 270)
    
    try:
        while cam.isOpened():
            _, frame = cam.read()
            
            qrDecoder = cv2.QRCodeDetector()
            data, bbox, recti = qrDecoder.detectANDndDecode(frame)
                
            cv2.imshow("frame", frame)
            lastline = ""
            
            if recti is not None:
                try:
                    with open("qrcode.txt", "r") as f:
                        lastline = f.readlines()[-1]
                except:
                    print("no file")
                
                print(data, lastline)
                
                if data in lastline:
                    print("same data")
                else:
                    print("save data")
                    with open("qrcode.txt","a"):
                        f.write(data + "\r\n")
                    time.sleep(3.0)
            
            keyCode = cv2.waitKey(10) & 0xFF
            # Stop the program on the ESC key or 'q'
            if keyCode == 27 or keyCode == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    
    cv2.destroyAllWindows()
    g.cleanup()
    
if __name__ == "__main__":
    main()