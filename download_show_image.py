import urllib.request
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
urllib.request.urlretrieve("IMAGE_URL", "IMAGE_NAME")
img=mpimg.imread('IMAGE_NAME')
imgplot = plt.imshow(img)
