
# Image Processing Project

This **Image Processing Project** is a Python-based program that uses the OpenCV library to detect colors and hand movements, triggering specific actions based on these visual inputs. The application demonstrates the power of computer vision in real-time image processing.

---

## Key Features

- **Color Detection**:
  - Detects specific colors in the video feed.
  - Triggers predefined actions based on the detected colors.
- **Hand Movement Recognition**:
  - Tracks hand movements in real-time.
  - Executes specific actions when predefined gestures are recognized.
- **Real-Time Processing**:
  - Processes video input from a webcam in real-time.

---

## Getting Started

### Prerequisites

- **Python** >= 3.7
- **OpenCV** (cv2 library)
- A webcam for capturing video input

---

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YazanM23/ImageProcessingProject
   cd ImageProcessingProject
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install opencv-python opencv-contrib-python numpy
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

---

## Usage

1. **Webcam Setup**:
   - Ensure your webcam is connected and accessible by the program.
   - The application will automatically use the primary webcam for input.

2. **Color Detection**:
   - OpenCV processes the video feed and detects specific colors.
   - Modify the `main.py` file to define actions for different colors.

3. **Hand Movement Recognition**:
   - Uses OpenCV's contour and shape detection features.
   - Modify the gesture logic in the `main.py` file to customize actions.

---

## File Structure

- **`main.py`**: Entry point of the program.
- **`requirements.txt`**: Lists all the Python dependencies.
- **`utils/`**: Contains helper functions for image processing (if applicable).

---

## Customization

- Modify the `color_ranges` in the `main.py` file to detect specific colors by adjusting HSV thresholds.
- Update the gesture logic to add or change actions triggered by hand movements.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Contact

For queries or feedback, reach out:

- **Name**: Yazan Mansour
- **Email**: Yazan.mansour2003@gmail.com
