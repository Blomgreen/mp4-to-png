import os, sys
import cv2

"""
video_path: Path to the video file
output_folder: Folder where the extracted frames will be saved
frames_between_savedImages: Number of frames to skip before saving the next frame
"""

# Command line arguments
if len(sys.argv) != 3:
    print("Usage: python main.py <video_file> <output_folder> <frames_between_savedImages>")
    sys.exit(1)

# Get the video file name, output folder and frames_between_savedImages from the command line arguments
video_path = sys.argv[1]
output_folder = sys.argv[2]
frames_between_savedImages = int(sys.argv[3])

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

frame_count = 0
while True:
    # Read the next frame from the video
    ret, frame = cap.read()
    if not ret:
        break  #Break the loop when no more frames are available

    # If the frame count is a multiple of frames_between_savedImages, save the frame
    if(frame_count%frames_between_savedImages == 0):
        frame_filename = os.path.join(outputFolder, f'frame_{frame_count:04d}.png')
        cv2.imwrite(frame_filename, frame)

    # Increment the frame count
    frame_count += 1

# Release the VideoCapture object
cap.release()

print(f"Extracted {frame_count} frames from the video.")
