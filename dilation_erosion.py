import cv2
from matplotlib import pyplot as plt
image_file = "data/ww1.png"
img = cv2.imread(image_file)
from binarization import img_bw,gray_img

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

#Erosion: Thinning the font

def thin_font(image):
    import numpy as np
    image=cv2.bitwise_not(image)
    kernel=np.ones((2,2),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.bitwise_not(image)
    return image

eroded_image=thin_font(img_bw)
cv2.imwrite("temp/eroded_image.png",img_bw)

#display("temp/eroded_image.png")


#Dilation : thickening the font
def thick_font(image):
    import numpy as np
    image=cv2.bitwise_not(image)
    kernel=np.ones((2,2),np.uint8)
    image=cv2.dilate(image,kernel,iterations=1)
    image=cv2.bitwise_not(image)
    return image

dilated_image=thick_font(gray_img)
cv2.imwrite("temp/dilated_image.png",gray_img)

display("temp/dilated_image.png")

