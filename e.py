import cv2

# Load an image
image = cv2.imread('path_to_your_image.jpg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
