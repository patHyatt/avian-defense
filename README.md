# Avian Defense Project

This project streams video from a webcam and uses YOLO for real-time object detection, specifically detecting cats.

## Prerequisites

- Python 3.8 or later
- A webcam connected to your system

## Installation

1. Clone this repository or download the project files.
2. Open a terminal in the project directory.
3. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. Ensure your webcam is connected.
2. Run the Python script:

   ```bash
   python cat_attack.py
   ```

3. The video stream will open, and the script will detect cats in real-time. Press `q` to exit the video stream.

## Notes

- The YOLO model used in this project is pre-trained and expects the COCO dataset class IDs. The class ID for cats is 15.
- Make sure your Python environment has access to the webcam and required libraries.