🖼️ Hologram Project – Gesture Controlled Image Viewer
📌 Overview

This project is a gesture-controlled hologram system that allows users to interact with images in a 3D-like holographic display using hand gestures. The project uses computer vision to detect hand movements and map them into commands such as swipe, drag, and move images in different directions.

The system is designed to work without any costly hardware – just a standard webcam and open-source libraries.

✨ Features

✅ Move images left, right, up, and down using your index finger
✅ Swipe gestures:

One finger up → Swipe Right

Two fingers up → Swipe Left
✅ Display multiple images and switch between them like a holographic slideshow
✅ Adjustable zoom to fit images perfectly inside the display frame
✅ Works in real-time with just a webcam

🛠️ Tech Stack

Programming Language: Python 🐍

Libraries/Frameworks:

OpenCV
 – for image processing & display

Mediapipe
 – for real-time hand tracking

NumPy
 – for array & mathematical operations

📂 Project Structure
hologram/
│── images/             # Folder containing images for hologram display
│── hologram.py         # Main script (gesture recognition + hologram display)
│── requirements.txt    # List of dependencies
│── README.md           # Project documentation

⚙️ Installation

Clone this repository

git clone https://github.com/Adityaa0206/hologram.git
cd hologram


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt

▶️ Usage

Place the images you want to use inside the images/ folder.

Run the program:

python hologram.py


Stand in front of your webcam and use gestures:

Drag index finger → Move image

Swipe with one finger → Next image

Swipe with two fingers → Previous image

🎯 Future Improvements

Add support for 3D model rotation

Implement gesture-based zoom in/out

Improve hand detection in low light conditions

Deploy as a desktop app with PyQt or Tkinter
