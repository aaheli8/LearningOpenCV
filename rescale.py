#Rescaling Images and Videos
import cv2 as cv

img=cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    # work for Images,Videos and Live Videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    
    dimensions=(width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    #Work fpr Live Videos
    capture.set(3,width)
    capture.set(4,height)
#Reading Videos in OpenCv
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(40) & 0xFF==ord('d'):
         break

capture.release()
#cv.waitKey(0)
cv.destroyAllWindows()