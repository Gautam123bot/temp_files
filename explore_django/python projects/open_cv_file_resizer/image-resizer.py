import cv2

# Configurable Parameters
# Percent by which the image is resized
scale_percent = 50
source = "my_img.jpg"
destination = 'newImage.jpeg'

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)


# Calculate the 50 percent of original dimesions
new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)

# cv2.waitKey(0)