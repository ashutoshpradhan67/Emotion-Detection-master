import cv2 
import urllib
print("Start")

# path 
path = "happy.png"

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2GRAY color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
image2 = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
image3=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)


# Displaying the image 
cv2.imshow("RGB2HSV", image)
cv2.imshow("BGR2HSV", image2)
cv2.imshow("COLOR_BGR2GRAY",image3)


cv2.waitKey(0)
cv2.destroyAllWindows()

