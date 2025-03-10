from PIL import Image

im_file="data/ww1.png"

im=Image.open(im_file)

im.show()
im.save("temp/ww1_copy.png")