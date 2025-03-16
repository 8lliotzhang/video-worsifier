#ASCIFY-PRINT WHILE PROCESSING
#Harry Chen, Elliot Zhang - March 15-16, Scrapyard Ottawa

#make sure yall have these
import os
from ascii_magic import AsciiArt
import cv2
import shutil


video = "videos/Rick Roll (Different link + no ads).mp4"

#try these videos!!
#"videos/【東方】Bad Apple!! ＰＶ【影絵】.mp4"
#"videos/Rick Roll (Different link + no ads).mp4"
#"videos/Shrek - All star _ Intro HD (1080p).mp4"



#takes a video, turns it into frames.
def FrameCapture(path, output_folder): 
    #purge folder - in case a shorter thing means previous frames aren't wiped out.
    shutil.rmtree(output_folder)
    #remake the folder if it doesn't exist. it should though.
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
        # idk I think chatgpt or deepseek did this but it works 
        success, image = vidObj.read() 

        if not success:
            break

        # Save the frames in the specified folder
        frame_path = os.path.join(output_folder, "frame%d.jpg" % count)
        cv2.imwrite(frame_path, image) 

        count = count + 1
        print(f"Frame {count} saved at {frame_path}")

    #put everything into the extracted_frames folder - defined at bottom.

def convert_frame(filename):
    if os.path.exists(filename):
        #AsciiVersion is the actual ASCII txt
        AsciiVersion = AsciiArt.from_image(filename).to_ascii()
        print(f"Processed {filename}")
        return AsciiVersion
    else:
        print(f"{filename} does not exist :(")
        return None


def PrintWhileProcess():
    print("let's go debug, frames: " + str(count))
    #make sure frames r good
    i = 0
    #ok, print out each frame in order
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
    #this doesn't do anything. 
    

if __name__ == "__main__":
    print('test')
    main()
    #download_with_cookies(video_url, cookies_path, output_path="videos")
        #this is left over when i was downloading vids the other day. Or today. The two kinda blended together
