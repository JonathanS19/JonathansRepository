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

