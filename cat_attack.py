from ultralytics import YOLO
import cv2
from playsound import playsound

# Define a constant for the class ID of cats
CAT_CLASS_ID = 15

# Load a pre-trained YOLO model
model = YOLO("yolo11n.pt")

# Open a video stream (0 for webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform object detection
    results = model.track(source=frame, show=True, stream=True, conf=0.6, classes=[CAT_CLASS_ID])

    # Filter results to detect only cats
    for result in results:
        for box in result.boxes:
            if box.cls == CAT_CLASS_ID:  # Use the constant for cat class ID
                print(f"Cat detected with confidence {box.conf}")
                playsound('right_answer.mp3', block=False)  # Play dog barking sound

    # Display the frame with detections
    cv2.imshow("Avian Defense", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()