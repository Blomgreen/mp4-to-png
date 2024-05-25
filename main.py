import cv2
import os

video_path = 'initial-data-video.mp4'

outputFolder = 'frames'
os.makedirs(outputFolder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0
frames_between_savedImages = 8 #Instead of saving all frames, only save every x frames
while True:
    ret, frame = cap.read()
    if not ret:
        break  #Break the loop when no more frames are available

    if(frame_count%frames_between_savedImages == 0):
        frame_filename = os.path.join(outputFolder, f'frame_{frame_count:04d}.png')
        cv2.imwrite(frame_filename, frame)

    frame_count += 1

cap.release()

print(f"Extracted {frame_count} frames from the video.")
