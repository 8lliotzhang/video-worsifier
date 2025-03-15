import os
from ascii_magic import AsciiArt
#HATE. LET ME TELL YOU HOW


# take frame i of input
# output frame i of ascii

def convertAllFrames():
    
    item_count = 0
    with os.scandir("extracted_frames") as entries:
        for entry in entries:
            item_count += 1
    
    totalFrames = item_count
    print("FINAL COUNT IS " + str(item_count))
    AsciiArray = []

    for i in range(totalFrames):     
        filename = f'extracted_frames/frame{i}.jpg'
        if os.path.exists(filename):
            print(filename + " exists yayayay")
            AsciiVersion = AsciiArt.from_image(filename)
            AsciiVersion.to_terminal()
            AsciiArray.append(AsciiArt.from_image(filename))
            
        else:
            print(filename + " does not exist :(")
    




#temp output - plan to STORE each frame, then display it frame by frame

convertAllFrames()