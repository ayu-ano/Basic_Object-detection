# Basic Object Detection using OpenCV

This repository contains code for basic object detection using OpenCV in Python. The code uses a simple background subtraction technique along with Euclidean distance-based tracking to detect and track objects in a video stream.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- NumPy


This script will use a pre-recorded video (`highway2.mp4`), apply background subtraction, detect objects, and track them using Euclidean distance.

## Customization

You can modify the following parameters in the `main.py` script:

- ROI (Region of Interest): Adjust the ROI to focus on a specific area in the video frame.
- Thresholds: Modify the thresholds used in background subtraction and contour detection to improve object detection accuracy.
- Keybindings: Press 'ESC' to exit the application.


## Acknowledgments

- Inspired by the [OpenCV](https://opencv.org/) library.


