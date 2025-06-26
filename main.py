import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("[ERROR] Cannot access webcam. Try a different camera index.")
    exit()

print("[INFO] Webcam successfully opened. Starting real-time detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to read from webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame, (x, y), (x + w, y + h), (0, 255, 0), 2
        )

    cv2.imshow("Real-Time Face Detection (Press 'q' to quit)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
