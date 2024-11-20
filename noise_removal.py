import cv2
from matplotlib import pyplot as plt
image_file = "data/ww1.png"
img = cv2.imread(image_file)
from binarization import img_bw,img

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


# do not need this to call as our original image is already very noise free
def noise_removal(image):
    import numpy as np
    kernel=np.ones((1,1),np.uint8)
    #dilation and erosion for font noise removal, also done separately
    image=cv2.dilate(image,kernel,iterations=1)
    kernel=np.ones((1,1),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    #median blur and morphology for bg noise removal
    image=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
    image=cv2.medianBlur(image,3)
    return image

no_noise=noise_removal(img_bw)
cv2.imwrite("temp/no_noise.png",no_noise)

#display("temp/no_noise.png")

