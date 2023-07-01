# Hand Gesture Volume Control

This program allows you to control the system volume using hand gestures captured from a webcam. It uses the OpenCV library to capture video frames, the Mediapipe library for hand tracking, and the pycaw library to control the audio volume.

## Dependencies

The following dependencies are required to run the program:

- OpenCV
- Mediapipe
- pycaw

You can install these dependencies using pip:

```shell
pip install opencv-python mediapipe pycaw
```

## Usage

1. Run the program by executing the script.
2. A window will open displaying the webcam feed with hand tracking overlays.
3. Extend your hand towards the camera and make sure your palm and fingers are visible.
4. Adjust the distance from the camera to ensure accurate hand tracking.
5. Control the system volume by moving your thumb and index finger closer or farther apart.
6. The program will calculate the length of the line between the thumb and index finger and map it to the system volume level.
7. The current volume level and a visual volume bar will be displayed on the screen.

## License

This program is licensed under the [MIT License](LICENSE).

## Acknowledgements

The hand tracking functionality in this program is based on the HandTrackingModule, which is a custom module using the Mediapipe library for hand tracking.
