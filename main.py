import pywhatkit as pwk
if __name__ == "__main__":
    input_image = "bwtest-sm.jpg"
    output_image = "ascii_out"

    pwk.image_to_ascii_art(input_image,output_image)

    with open(output_image+".txt","r") as f:
        print(f.read())