import cv2
import os

def FrameCapture(path, output_folder): 

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Path to video file 
    vidObj = cv2.VideoCapture(path) 

    # Used as counter variable 
    count = 0

    # checks whether frames were extracted 
    success = 1

    while success: 

        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 

        if not success:
            break

        # Save the frames in the specified folder
        frame_path = os.path.join(output_folder, "frame%d.jpg" % count)
        cv2.imwrite(frame_path, image) 

        count += 1
        print(f"Frame {count} saved at {frame_path}")



# Specify the output folder
output_folder = "extracted_frames"
# Calling the function 
FrameCapture("videoplayback.mp4", output_folder)
