
from PIL import Image
import matplotlib.pyplot as plt
import os
import random


current_folder = os.path.dirname(os.path.abspath(__file__))

def display_pictures(pics_path: list):
    fig, ax = plt.subplots(2, 2)
    ax[0, 0].imshow(pics_path[0])
    ax[0, 1].imshow(pics_path[1])
    ax[1, 0].imshow(pics_path[2])
    ax[1, 1].imshow(pics_path[3])

    for i in range(2):
        for j in range(2):
            ax[i, j].axis('off')

    plt.show()

#display_pictures([Image.open(os.path.join(current_folder, 'pic10.png')), Image.open(os.path.join(current_folder, 'pic3.png')), Image.open(os.path.join(current_folder, 'pic6.png')), Image.open(os.path.join(current_folder, 'pic12.png'))])


all_pics = {current_folder + '\pic1.png':'0000', current_folder + '\pic2.png':'0001', current_folder + '\pic3.png':'0010', current_folder + '\pic4.png':'0011',
            current_folder + '\pic5.png':'0100', current_folder + '\pic6.png':'0101', current_folder + '\pic7.png':'0110', current_folder + '\pic8.png':'0111',
            current_folder + '\pic9.png':'1000', current_folder + '\pic10.png':'1001', current_folder + '\pic11.png':'1010', current_folder + '\pic12.png':'1011',
            current_folder + '\pic13.png':'1100', current_folder + '\pic14.png':'1101', current_folder + '\pic15.png':'1110', current_folder + '\pic16.png':'1111'}

# homework 1 :
# 2 (4)Bit-strings are similar if they have at least 3 same bits at same positions
def is2bit_string_similar(bit_str1: str, bit_str2: str) -> bool:
    counter = 0
    for i in range(0,len(bit_str1)):
        if bit_str1[i] == bit_str2[i]:
            counter += 1
    if counter > 2:
        return True
    if counter < 3:
        return False




# homework 2 fix the line 56 using the function is2bit_string_similar:
def search_bit_string(bit_str: str) -> list[str]:
    # sample bit_str: "1?01"  1?01 and 1101 are similar
    # sample output: ['pic1.png', 'pic2.png']
    result = []
    for key, value in all_pics.items():
        if is2bit_string_similar(bit_str, value) == True: # value is similar to the bit_str
            result.append(key.split("\\")[-1])
    return result



# homework 3: complete following using search_bit_string
def complete_bit_string(bit_str_list: list) -> list:
    # sample pics is list of 2 bit-strings, e.g ["1001",,, "1011"]
    # sample pics is list of 4 bit-strings, e.g ["pic10.png", "pic3.png", "pic6.png", "pic12.png"]
    first_bit_string = bit_str_list[0]
    
   
    fourth_bit_string = bit_str_list[1]

    second_bit_string = first_bit_string[1] + "?" + first_bit_string[3] + fourth_bit_string[1]
    second_bit_string = search_bit_string(second_bit_string)[0]




    third_bit_string = first_bit_string[2] + first_bit_string[3] + "?" + fourth_bit_string[2]
    third_bit_string = search_bit_string(third_bit_string)[0]

    first_bit_string = search_bit_string(first_bit_string)[0]
    fourth_bit_string = search_bit_string(fourth_bit_string)[0]
    return [first_bit_string, second_bit_string, third_bit_string, fourth_bit_string]

# homework 4: choose 2 random pictures from all_pics, use function complete_bit_string to get complete list of 4 pictures
# and display them using function "display_pictures".
# Choose 2 random pictures

import random
from random import sample

random_pics = random.sample(list(all_pics.keys()), 2)
bit_str_list = [all_pics[pic] for pic in random_pics]
complete_list = complete_bit_string(bit_str_list)
display_pictures([Image.open(os.path.join(current_folder, pic)) for pic in complete_list])