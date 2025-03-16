#ASCIFY-PRINT WHILE PROCESSING
import os
from ascii_magic import AsciiArt
import cv2
import shutil


video = "videos/Rick Roll (Different link + no ads).mp4"
#"videos/【東方】Bad Apple!! ＰＶ【影絵】.mp4"
#"videos/Rick Roll (Different link + no ads).mp4"
#"videos/Shrek - All star _ Intro HD (1080p).mp4"





def FrameCapture(path, output_folder): 
    #purge folder - in case a shorter thing references
    shutil.rmtree(output_folder)
    #remake it if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
    global count 
    count = 0
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

        count = count + 1
        print(f"Frame {count} saved at {frame_path}")
    
    output_folder = "extracted_frames"

def convert_frame(filename):
    if os.path.exists(filename):
        AsciiVersion = AsciiArt.from_image(filename).to_ascii()
        print(f"Processed {filename}")
        return AsciiVersion
    else:
        print(f"{filename} does not exist :(")
        return None


def PrintWhileProcess():
    print("let's go debug, frames: " + str(count))
    i = 0
    while i < count:
        print("_____________")
        filen = "extracted_frames/frame"+str(i)+".jpg"
        AsciiVersion = AsciiArt.from_image(filen).to_ascii()
        print(AsciiVersion)
        i += 1




def main():
    #playsound('audio.mp3')
    FrameCapture(video, "extracted_frames")
    PrintWhileProcess()
    print('anim done')

    #CHANGE THE FPS HERE
    fps = 20 
    

if __name__ == "__main__":
    print('test')
    main()
    #download_with_cookies(video_url, cookies_path, output_path="videos")
