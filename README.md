Real-Time Face Detection with OpenCV

This is a beginner-friendly computer vision project that performs real-time face detection using a webcam and OpenCV's Haar Cascade classifier. It captures video from your webcam, detects faces in each frame, and displays bounding boxes around them.

Features

Real-time video capture from webcam

Face detection using Haar cascade classifier

Bounding box visualization around detected faces

Cross-platform support (Windows, macOS, Linux)

Prerequisites

Python 3.7+

Webcam (built-in or external)

macOS users: Ensure terminal or IDE has camera access under System Settings → Privacy & Security → Camera

Installation

Clone the repository:

git clone https://github.com/SenuriR/Real-Time-Face-Recognition.git
cd real-time-face-detection

Install dependencies:

pip install opencv-python

Running the Project

To start the face detection script:

python main.py

If you're using macOS and want to ensure AVFoundation is used (recommended for compatibility), use:

cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

How It Works

A Haar cascade classifier is loaded from OpenCV’s pre-trained models.

The webcam captures frames in real time.

Each frame is converted to grayscale.

The classifier detects faces and returns bounding box coordinates.

Rectangles are drawn around each detected face.

Press q to exit the application.

Troubleshooting

If the webcam does not work, try using a different camera index (0, 1, 2...).

On macOS, ensure your terminal has camera access in System Settings.

If no faces are detected, check lighting and position.

Credits

OpenCV (https://opencv.org/)

Haar cascade face detection models provided by OpenCV


