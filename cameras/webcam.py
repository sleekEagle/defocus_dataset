import cv2

def list_available_cameras(max_cameras=10):
    """Test camera IDs from 0 to max_cameras-1"""
    available = []
    
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            # Try to read a frame to confirm it's really working
            ret, frame = cap.read()
            if ret:
                print(f"✓ Camera ID {i} is available and working")
                available.append(i)
            else:
                print(f"? Camera ID {i} opens but cannot read frames (may be in use)")
            cap.release()
        else:
            print(f"✗ Camera ID {i} is not available")
    
    return available

def grab_frame(cam_id):
    cap = cv2.VideoCapture(cam_id, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print(f"Error: Could not open camera with ID {cam_id}")
        return False
    
    # Disable auto features (if supported by your webcam)
    # cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # Disable auto focus
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)  # Disable auto exposure (0.25 = manual mode)
    # cap.set(cv2.CAP_PROP_AUTO_WB, 1)  # 1 = Disable auto white balance
    
    # Set manual values (adjust these as needed)
    # Lower values = more blue, higher = more yellow/red
    # cap.set(cv2.CAP_PROP_WB_TEMPERATURE,5000)  # Try 4000-6500 range
    cap.set(cv2.CAP_PROP_EXPOSURE, -4)  # Exposure value (negative = darker)
    # cap.set(cv2.CAP_PROP_BRIGHTNESS, 0)  # 0-255
    # cap.set(cv2.CAP_PROP_CONTRAST, 32)   # 0-255
    # cap.set(cv2.CAP_PROP_SATURATION, 32) # 0-255

    ret, frame = cap.read()
    if ret:
        cap.release()
        return frame
    else:
        print(f"Error: Could not read frame from camera with ID {cam_id}")
        cap.release()
        return False
    

def test_camera(cam_id):
    frame = grab_frame(cam_id)
    if frame is not False:
        print(f"Successfully captured frame from camera {cam_id}")
        print(f"Frame shape: {frame.shape}")
        print(f"Frame size: {frame.size} bytes")
    else:
        print(f"Failed to capture frame from camera {cam_id}")

def show_frame(frame):
    cv2.imshow('Camera Frame - Press any key to close', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # list_available_cameras()
    camera_id = 1
    test_camera(camera_id)
    frame = grab_frame(camera_id)
    if frame is not False:
        show_frame(frame)
    pass

