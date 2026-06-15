import cv2
import numpy as np

# Video settings
width, height = 640, 480
fps = 24
duration = 5  # seconds

# Create video writer
video = cv2.VideoWriter(
    "ai_video.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

# AI-generated text (example)
ai_text = "Welcome to AI Video Generator"

# Generate frames
for i in range(fps * duration):
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Background color animation
    frame[:] = (i % 255, 100, 150)

    # Add AI text
    cv2.putText(
        frame,
        ai_text,
        (50, height // 2),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    video.write(frame)

video.release()

print("Video generated successfully: ai_video.mp4")