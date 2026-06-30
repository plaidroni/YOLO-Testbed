import cv2

def find_camera_index():
    print("Checking for available camera indexes...")
    # Loop through indexes 0 to 4 (most common range for laptops)
    for index in range(5):
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW) # CAP_DSHOW optimizes Windows discovery
        if cap.isOpened():
            # Try to read a frame to confirm it is fully functional
            ret, frame = cap.read()
            if ret:
                print(f"  [SUCCESS] Found working camera at index: {index}")
            else:
                print(f"  [WARNING] Index {index} opened but could not read a frame.")
            cap.release()
        else:
            print(f"  [FAILED] No camera found at index: {index}")

if __name__ == "__main__":
    find_camera_index()
    input("\nPress ENTER to exit...")