# Basic Object Detection using OpenCV

This repository contains code for basic object detection using OpenCV in Python. The code uses a simple background subtraction technique along with Euclidean distance-based tracking to detect and track objects in a video stream.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- NumPy

## Screenshots
![Screenshot](https://github-production-user-asset-6210df.s3.amazonaws.com/152168191/347328873-4a177c78-bbf9-485b-b975-2a4ed20ee580.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240806%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240806T171402Z&X-Amz-Expires=300&X-Amz-Signature=79c789eee299a0a40f72a327ff557abb828f68cd89ef78bfca31657529ab52cb&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=771737081)

This script will use a pre-recorded video (`highway2.mp4`), apply background subtraction, detect objects, and track them using Euclidean distance.

## Customization

You can modify the following parameters in the `main.py` script:

- ROI (Region of Interest): Adjust the ROI to focus on a specific area in the video frame.
- Thresholds: Modify the thresholds used in background subtraction and contour detection to improve object detection accuracy.
- Keybindings: Press 'ESC' to exit the application.


## Acknowledgments

- Inspired by the [OpenCV](https://opencv.org/) library.


