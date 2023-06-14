#importing dependencies
import cv2

#reading the image
image = cv2.imread("C:\kaam ka\dog.jpg")
cv2.imshow("Dog", image)
cv2.waitKey(0)

#creating a new image by converting the original image to greyscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Dog", gray_image)
cv2.waitKey(0)

#inverting the new grayscale image
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

#making the image blur
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

#inverting the blur image so that we can convert the image into a pencil sketch
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

#Finally looking both at our original image amd pencil sketch
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)