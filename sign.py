from PIL import Image

# Takes in image of all sign language gestures

im = Image.open("sign.png")


xcent = im.width/2
ycent = im.height/2

images = []

# Creates crop images function that adjusts the cropped image based on the different sign language gestures
def cropImages(rowLength,incrementorOne,incrementorTwo,valOne = 380, valTwo = 680):

    for _ in range(rowLength):
        x1 = xcent - valOne
        valOne -= 112
        y1 = ycent + incrementorOne

        x2 = im.width - valTwo
        valTwo -= 112
        y2 = im.height + incrementorTwo

        cropped = im.crop((x1, y1, x2, y2))
        images.append(cropped)
 

# Calls the function with the different row lengths and locations

cropImages(7, -315, -495)
cropImages(7, -150, -330)
cropImages(7, 15, -165)
cropImages(5, 180, 0)
cropImages(1, 180, 0, -58, 195)

# Converts the alphabet to alphanumerical letters
def alphabet(audio4):

    letters = audio4

    numb = []

    for letter in letters:
        number = ord(letter) - 96
        numb.append(number)
        
    # Shows the images in accordance with the position
    print(numb)
    counter = 0
    for i in range(len(numb)):
        j = numb[i]
        images[j-1].show()
        for i in range(len(numb)):
            counter = counter + 1
