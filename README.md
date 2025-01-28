# Parking Space Counter

This project implements a Parking Space Counter system that identifies free and occupied parking spaces from a video feed. The system uses pre-defined parking space coordinates, processes video frames to analyze the spaces, and provides real-time feedback on the availability of parking spots.

## Features
- Define and store parking space coordinates using mouse interactions.
- Real-time detection of free and occupied parking spaces.
- Outputs the video with visual indicators for parking space status.
- Displays the count of available parking spaces on the video.

## Requirements
- Python 3.7+
- Libraries:
  - `opencv-python`
  - `cvzone`
  - `numpy`
  - `pickle`

Install dependencies using:
```bash
pip install opencv-python-headless cvzone numpy
```

## How It Works
### File Descriptions
1. **`parking_space.py`**
   - Allows the user to define parking spaces by clicking on the video feed.
   - Left-click to add parking spaces, and right-click to remove them.
   - Stores the parking space coordinates in a pickle file (`carParkPos2`).

2. **`main.py`**
   - Processes a video feed to analyze parking spaces based on the coordinates stored in `carParkPos2`.
   - Uses image processing techniques to detect free and occupied spaces.
   - Displays the count of free spaces and outputs a video with visual feedback.

### Steps
1. **Defining Parking Spaces**:
   - Run `parking_space.py`.
   - Left-click to add parking spaces and right-click to remove them.
   - The coordinates are automatically saved to the file `carParkPos2`.

2. **Analyzing Parking Spaces**:
   - Run `main.py`.
   - The script reads the stored coordinates and analyzes the video feed to determine parking space occupancy.
   - Displays the processed video with the following visual feedback:
     - **Green rectangles** for free spaces.
     - **Red rectangles** for occupied spaces.

3. **Output Video**:
   - The processed video is saved as `parking_space_counter.mp4`.

## Customization
- Update the `w` and `h` variables in both scripts to change the parking space rectangle size.
- Replace the input video file in `main.py` with your own video for analysis.
- Adjust the threshold value in `checkParkingSpace` to calibrate detection sensitivity.

## Notes
- Ensure that the video resolution matches the scale of defined parking spaces for accurate detection.
- Use clear and properly lit parking lot videos for best results.

## License
This project is for educational and non-commercial purposes.

