#Basic Functions 
import cv2 as cv

def sized(img,scale = 0.3):
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_LINEAR)


img = cv.imread("dubai.jpg")
newimg = sized(img)
#cv.imshow("Orginal",newimg)

#Grayscale conversion 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
newgray = sized(gray)
#cv.imshow("Grascale image",newgray)


#Blurring the image to reduce the noise
blur = cv.GaussianBlur(img,(15,15),cv.BORDER_DEFAULT)#The kernel must always be odd and by increasing the value you can increase the blur
newblur = sized(blur)
#cv.imshow("BlurredImg",newblur)

#Finding the edges/edge cascade 
#we are using canny which is famous in the computer vision world

edge = cv.Canny(img,125,145)
newedge = sized(edge)
#cv.imshow("Edges with Noise",newedge) 


# * * * * * * * * * #
#Dilating or increasing the thickness of the edges
dilated = cv.dilate(edge,(7,7),iterations=3)
newdil = sized(dilated)
cv.imshow("Dilated Image",newdil)

#Eroding or reducing the thickness of the edges 
erode = cv.erode(dilated,(7,7),iterations=4)
newerode = sized(erode)
cv.imshow("Eroded image",newerode)

#Resize image
resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)#No need to include interpolation a default value is assigned and if we use intercubic its the slowest by produces the highest quality image 
cv.imshow("Resized img",resize)#also using this function aspect ratio is not cared for

#Cropping a image

crop = img[125:200,250:500]
cv.imshow("Cropped img",crop)

cv.waitKey(0)

#Practice 1
import cv2 as cv
import numpy as np

img = cv.imread("cat.jpg")

def resiz(img,scale=0.75):
    width = int(img.shape[1]*scale*4)
    height = int(img.shape[0]*scale*4)

    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_LINEAR)

newimg = resiz(img)
cv.imshow("Resized Image",newimg)
"""
#Grayscale conversion
gray = cv.cvtColor(newimg,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image",gray)

#Blurred Image
blur = cv.GaussianBlur(newimg,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blurred Image",blur)

#Edges
edge = cv.Canny(newimg,125,145)
cv.imshow("Edges of a Image",edge)


#You can enhance the edges using blurring or be more refined i guess
edge2 = cv.Canny(blur,125,145)
cv.imshow("Refined Edges",edge2)


#Dilate a Image that is to increase the thickness of the edges 
dilate = cv.dilate(edge,(7,7),iterations=3)
cv.imshow("Dilated Image",dilate)#Doesnt work on normal images we need to find the edges first 

#Erode the image this is used to reverse the dilation or to reduce the thickness of the edges 
erode = cv.erode(dilate,(7,7),iterations=4)
cv.imshow("Eroded Image",erode)
"""
def translate(img,x,y):
    tramat = np.float32([[1,0,x],[0,1,y]])
    (height,width) = (img.shape[:2])

    dimensions = (width,height)
    return cv.warpAffine(newimg,tramat,dimensions)

transimg = translate(newimg,100,100) 
cv.imshow("Translated Image",transimg)

#To rotate a image
def rotate(img,angle,rotpoint=None):
    (height,width) = (img.shape[:2])
    dimensions = (width,height)

    if rotpoint == None:
        rotpoint  = (width//2,height//2)

    rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)

    return cv.warpAffine(img,rotmat,dimensions)

rotimg = rotate(newimg,120)
cv.imshow("Rotated Image",rotimg)

#To resize a image auto and not manually 
resizeauto = cv.resize(img,(700,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Autosize",resizeauto)

cv.waitKey(0)
