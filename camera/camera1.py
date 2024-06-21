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

def show_camera():
    window_title = "CSI Camera"

    gstream = gstreamer_pipeline(flip_method=2)
    
    print(gstream)
    cam = cv2.VideoCapture(gstream, cv2.CAP_GSTREAMER)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 270)
    
    while cam.isOpened():
        _, frame = cam.read()
        # Check to see if the user closed the window
        # Under GTK+ (Jetson Default), WND_PROP_VISIBLE does not work correctly. Under Qt it does
        # GTK - Substitute WND_PROP_AUTOSIZE to detect if window has been closed by user
        cv2.imshow(window_title, frame)
        
        keyCode = cv2.waitKey(10) & 0xFF
        # Stop the program on the ESC key or 'q'
        if keyCode == 27 or keyCode == ord('q'):
            break
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_camera()