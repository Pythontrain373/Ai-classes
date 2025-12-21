#Image resizer
import cv2
small_image = cv2.imread('small_image.jpg')
resized_image = cv2.resize(small_image, (200, 200))
cv2.imwrite('small_image_resized.jpg', resized_image)

middle_image = cv2.imread('middle_image.jpeg')
resized_image = cv2.resize(middle_image, (400, 400))
cv2.imwrite('middle_image_resized.jpg', resized_image)

large_image = cv2.imread('large _mage.jpg')
resized_image = cv2.resize(large_image, (800, 800))
cv2.imwrite('large_image_resized.jpg', resized_image)

print('The images are resized')