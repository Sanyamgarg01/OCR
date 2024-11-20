import cv2
from matplotlib import pyplot as plt
image_file = "data/ww1.png"
img = cv2.imread(image_file)

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

def grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray_img=grayscale(img)
cv2.imwrite("temp/grey_image.png",gray_img)
#display("temp/grey_image.png")

thresh,img_bw=cv2.threshold(gray_img,160,200,cv2.THRESH_BINARY)
cv2.imwrite("temp/bw_img.png",img_bw)
#display("temp/bw_img.png")