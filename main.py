import cv2

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Try to open webcam (try other indexes if 0 doesn't work)
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("[ERROR] Cannot access webcam. Try a different camera index.")
    exit()

print("[INFO] Webcam successfully opened. Starting real-time detection...")

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to read from webcam.")
        break

    # Convert to grayscale for better face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame, (x, y), (x + w, y + h), (0, 255, 0), 2
        )

    # Show frame
    cv2.imshow("Real-Time Face Detection (Press 'q' to quit)", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] Quitting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
