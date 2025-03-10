#for inconsitent borders

import cv2
from matplotlib import pyplot as plt
new=cv2.imread("data/bordered.jpg")
import numpy as np




#https://stackoverflow.com/questions/28816046/
#displaying-different-images-with-actual-size-in-matplotlib-subplot
#no need to understand this code
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()


def remove_border(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contour,hierarchy=cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted=sorted(contour,key=lambda x:cv2.contourArea(x))
    cnt=cntsSorted[-1]
    x,y,w,h=cv2.boundingRect(cnt)
    crop=image[y:y+h,x:x+w]
    return(crop)

no_border=remove_border(new)
cv2.imwrite("temp/removed_border.jpg",no_border)
display("temp/removed_border.jpg")