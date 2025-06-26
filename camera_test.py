import cv2

# Try FaceTime HD Camera (index 0); change to 1 or 2 for iPhone cameras
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("[ERROR] Cannot access the selected webcam.")
    exit()

print("[INFO] Webcam connected. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Frame not received.")
        break

    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
