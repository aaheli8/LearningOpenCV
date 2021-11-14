import cv2 as cv

img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
#the img() value has to odd numbers only
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

# Dilating the image
dilated =cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)

# Eroding
eroded=cv.erode(dilated,(3,3), iterations=1)
cv.imshow('Eroding',eroded)

# Resize
resize=cv.resize(img,(500,500))
cv.imshow('Resize',resize)

#Cropping
cropped=img[50:200,200:400]
cv.imshow('Crop',cropped)


cv.waitKey(0)
