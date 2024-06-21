# -*- coding: utf-8 -*-

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
    
    LED = [4,17,18]
    g.setwarnings(False)
    g.setmode(g.BCM)
    
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)

    gstream = gstreamer_pipeline(flip_method=2)
    
    print(gstream)
    cam = cv2.VideoCapture(gstream, cv2.CAP_GSTREAMER)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 270)
    
    try:
        while cam.isOpened():
            _, frame = cam.read()
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            upper_red = (150,50,50)
            lower_red = (180,255,255)
            upper_green = (50,150,50)
            lower_green = (80,255,255)
            upper_blue = (100,100,120)
            lower_blue = (150,255,255)
            
            redMask = cv2.inRange(hsv, lower_red, upper_red)
            greenMask = cv2.inRange(hsv, lower_green, upper_green)
            blueMask = cv2.inRange(hsv, lower_blue, upper_blue)
            
            redPixels = cv2.countNonZero(redMask)
            greenPixels = cv2.countNonZero(greenMask)
            bluePixels = cv2.countNonZero(blueMask)
            
            colorList = [redPixels, greenPixels, bluePixels]
            maxValue = max(colorList)
            maxPos = colorList.index(maxValue)
            
            if maxValue > 300:
                if maxPos == 0:
                    g.output(LED[0],1)
                    g.output(LED[1],0)
                    g.output(LED[2],0)
                elif maxPos == 1:
                    g.output(LED[0],0)
                    g.output(LED[1],1)
                    g.output(LED[2],0)
                elif maxPos == 2:
                    g.output(LED[0],0)
                    g.output(LED[1],0)
                    g.output(LED[2],1)
                
            cv2.imshow("frame", frame)
            
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