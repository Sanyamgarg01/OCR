import cv2
from matplotlib import pyplot as plt
from remove_border import no_border

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

#display(image_file)

color=[255,255,255]
top,bottom,left,right=[150]*4
img_border=cv2.copyMakeBorder(no_border,top,bottom,left,right,cv2.BORDER_CONSTANT,value=color,)

cv2.imwrite("temp/img_border.jpg",img_border)
display("temp/img_border.jpg")