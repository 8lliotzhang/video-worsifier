import os
from ascii_magic import AsciiArt
#HATE. LET ME TELL YOU HOW


# take frame i of input
# output frame i of ascii

def convertAllFrames():
    totalFrames = 301
    AsciiArray = []

    for i in range(totalFrames):     
        filename = f'frame{i}.jpg'
        if os.path.exists(filename):
            print(filename + "exists yayayay")
            AsciiArray[i].append(AsciiArt.from_image(filename))
            print(AsciiArray[i])
        else:
            print(filename + " does not exist :(")
    








my_art = AsciiArt.from_image('erm.png')
#replace with CURRENT FRAME

output = my_art.to_ascii()
#convert to the ascii


print(output) 
#temp output - plan to STORE each frame, then display it frame by frame

convertAllFrames()