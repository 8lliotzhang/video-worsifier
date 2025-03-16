import os
import time
from ascii_magic import AsciiArt
from playsound import playsound
from threading import Thread

# Function to convert all frames to ASCII art and store them in text files
def convertAllFrames():
    # Create a folder to store the ASCII text files
    output_folder = "ascii_frames"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    item_count = 0
    with os.scandir("extracted_frames") as entries:
        for entry in entries:
            item_count += 1
    
    totalFrames = item_count
    print("FINAL COUNT IS " + str(item_count))

    for i in range(totalFrames):     
        filename = f'extracted_frames/frame{i}.jpg'
        if os.path.exists(filename):
            # Convert the image to ASCII art
            AsciiVersion = AsciiArt.from_image(filename).to_ascii()
            
            # Write the ASCII art to a text file (zero-padded)
            output_filename = f'{output_folder}/frame{i:04d}.txt'  # Zero-padded to 4 digits
            with open(output_filename, 'w') as f:
                f.write(AsciiVersion)
            
            print(f"Saved {output_filename}")
        else:
            print(filename + " does not exist :(")

# Function to display ASCII frames from text files at a specified FPS
def displayFrames(fps):
    output_folder = "ascii_frames"
    frame_delay = 1.0 / fps  # Calculate the delay between frames
    
    # Get the list of ASCII text files and sort them numerically
    ascii_files = sorted(
        [f for f in os.listdir(output_folder) if f.endswith('.txt')],
        key=lambda x: int(x[5:-4])  # Extract frame number from filename
    )
    # Preload all frames into memory
    frames = []
    for ascii_file in ascii_files:
        file_path = os.path.join(output_folder, ascii_file)
        with open(file_path, 'r') as f:
            frames.append(f.read())
    
    # Display each frame with precise timing
    start_time = time.perf_counter()
    for frame in frames:
        # Clear the console (optional, for better display)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the ASCII art
        print(frame)
        # Calculate the time to sleep to maintain FPS
        elapsed_time = time.perf_counter() - start_time
        sleep_time = max(0, frame_delay - elapsed_time)
        time.sleep(sleep_time)
        # Reset the start time for the next frame
        start_time = time.perf_counter()

# Function to play audio with a delay
def play_audio(delay):
    time.sleep(delay)  # Wait for the specified delay before playing audio
    playsound('audio.mp3', False)

# Main function
def main():
    # Convert frames to ASCII (if not already done)
    if not os.path.exists("ascii_frames"):
        convertAllFrames()
    
    fps = 30  # Specify the desired FPS
    audio_delay = 1.1  # Delay in seconds before audio starts (adjust as needed)
    
    # Start audio playback in a separate thread with a delay
    audio_thread = Thread(target=play_audio, args=(audio_delay,))
    audio_thread.start()
    
    # Start displaying frames
    displayFrames(fps)
    
    # Wait for the audio thread to finish
    audio_thread.join()

if __name__ == "__main__":
    main()

    