
# step 1: 
# e.g. {"c:\...\": "0101","c:\...\pic2.png": "0102", ...}

# step 2: create a function with list of 2 pics,   as inputs, with 4 pics as outputs


# Sample to show 4 pictures side by side with 2 pictures in each row

from PIL import Image
import matplotlib.pyplot as plt

# Open the images
import os
current_folder = os.path.dirname(os.path.abspath(__file__))
print(current_folder)
# [[0,0, 0, 0], [0,0,0,1], ..]

img1 = Image.open(current_folder + '\pic1.png')
path1 = current_folder + '\pic1.png'
img2 = Image.open(current_folder + '\pic2.png')
path2 = current_folder + '\pic2.png'
img3 = Image.open(current_folder + '\pic3.png')
path3 = current_folder + '\pic3.png'
img4 = Image.open(current_folder + '\pic4.png')
path4 = current_folder + '\pic4.png'
img5 = Image.open(current_folder + '\pic5.png')
path5 = current_folder + '\pic5.png'
img6 = Image.open(current_folder + '\pic6.png')
path6 = current_folder + '\pic6.png'
img7 = Image.open(current_folder + '\pic7.png')
path7 = current_folder + '\pic7.png'
img8 = Image.open(current_folder + '\pic8.png')
path8 = current_folder + '\pic8.png'
img9 = Image.open(current_folder + '\pic9.png')
path9 = current_folder + '\pic9.png'
img10 = Image.open(current_folder + '\pic10.png')
path10 = current_folder + '\pic10.png'
img11 = Image.open(current_folder + '\pic11.png')
path11 = current_folder + '\pic11.png'
img12 = Image.open(current_folder + '\pic12.png')
path12 = current_folder + '\pic12.png'
img13 = Image.open(current_folder + '\pic13.png')
path13 = current_folder + '\pic13.png'
img14 = Image.open(current_folder + '\pic14.png')
path14 = current_folder + '\pic14.png'
img15 = Image.open(current_folder + '\pic15.png')
path15 = current_folder + '\pic15.png'
img16 = Image.open(current_folder + '\pic16.png')
path16 = current_folder + '\pic16.png'

imagelist = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16]
pathlist = [path1, path2, path3, path4, path5, path6, path7, path8, path9, path10, path11, path12, path13, path14, path15, path16]
#Write a function, that get all pictures from current directory to a dictionary with the filename as key and the bit-content as value; For example: {"c:\...\pic1.png": "0101","c:\...\pic2.png": "0102", ...} and use the imagelist; The value of each picture comes from the following conditions: The first nubmer is the top left corner. 0 means water and 1 means land. The second number is the top right corner. The third number is the bottom left corner. The fourth number is the bottom right corner. The numbers are in binary format. For example: 0101 means water in the top left and bottom left corner and land in the top right and bottom right corner.And if the pixels aret the RGB (0,185,242) or (136,201,70) then jump to the next best corner.
def get_image_terrain(img):
    image_terrain = {}
    pixels = img.load()
    width, height = img.size
    corners = [(0, 0, 1, 1), (width - 1, 0, -1, 1), (0, height - 1, 1, -1), (width - 1, height - 1, -1, -1)]
    image_terrain[img.filename] = ""  # Initialize to empty string
    for corner in corners:
        x, y, dx, dy = corner
        for _ in range(width // 4):  # Only check a quarter of the image from the corner
            if pixels[x, y] == (0,185, 242, 255):  # water is represented by blue color
                terrain = "0"
                break
            elif pixels[x, y] == (136, 201, 70,255):  # land is represented by specific green color
                terrain = "1"
                break
            else:
                x += dx
                y += dy
        else:
            terrain = "X"  # if the pixel color does not match either land or water
        image_terrain[img.filename] += terrain
    return image_terrain

diciontary = {}
for i in range(1,16):
    diciontary[pathlist[i]] = get_image_terrain(imagelist[i])




# Use the function with a single image
"""
# Create four subplots
fig, ax = plt.subplots(2, 2)

# Display the images
ax[0, 0].imshow(img1)
ax[0, 1].imshow(img2)
ax[1, 0].imshow(img3)
ax[1, 1].imshow(img4)

# Remove the axes
for i in range(2):
    for j in range(2):
        ax[i, j].axis('off')



plt.show()

# homework till 20240313
# Eine lauffähige version von Aufgabe 1 in Github zu haben.
"""