# ✨ AI-Based Virtual Mouse using Hand Gestures

A Python-powered **Virtual Mouse** that enables you to control your computer cursor using just hand gestures detected via a webcam. No physical mouse required!

## 🚀 Features

- 🖱️ **Cursor Movement** — Move the mouse by moving your **index finger**.
- 👈 **Left Click** — Touch **thumb tip and index finger tip** to click.
- 👉 **Right Click** — Touch **thumb tip and middle finger tip** to right-click.
- 🔃 **Scroll Up** — Touch **thumb tip and ring finger tip (top)** to scroll up one viewport.
- 🔽 **Scroll Down** — Touch **thumb tip and ring finger base** to scroll down one viewport.
- 🖐️ **Drag & Drop** — Bring **thumb tip near index base and hold for 2 seconds** to start dragging. Release fingers to drop.

## 🧰 Technologies Used

- **Python 3.x**
- [OpenCV](https://opencv.org/) — Computer vision for webcam input.
- [MediaPipe](https://google.github.io/mediapipe/) — Real-time hand landmark detection.
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) — GUI automation (mouse control).


## 🎥 Demo Video

The demo video file (`Virtual Mouse Project Video.mp4`) is included in this repository.

Since the file size is large, GitHub might not preview it directly in the browser.

### 📌 To view the video:

1. Click the **"🔽" (Down arrow) button** at the top-right corner of the file list (beside the pencil/edit icon).
2. Select **"Open in github.dev"**.
3. In GitHub.dev, locate the `Virtual Mouse Project Video.mp4` file and click it to play.

Alternatively, you can download the file directly to view it on your device.


 <!-- Optional: Replace with your image or GIF -->

## 📂 How to Run

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/virtual-mouse.git
    cd virtual-mouse
    ```

2. Install dependencies:

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

3. Run the script:

    ```bash
    python virtual_mouse.py
    ```

4. Show your hand in front of the camera and control the mouse!

## ⚠️ Important Notes

- Run in a **well-lit environment** for best hand tracking.
- Webcam required.
- Avoid sudden hand movements to reduce lag.
- Adjust distance thresholds in the script for your comfort.

## 💡 Future Improvements

- Multi-hand support.
- Gesture customization via UI.
- Voice command integration.

## 🤝 Acknowledgements

- Inspired by tutorials and docs from OpenCV, MediaPipe, and PyAutoGUI communities.
- Special thanks to Google for MediaPipe framework.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

