import cv2 as cv
import numpy as np
import datetime
from matplotlib import pyplot as plt

'''img=cv.imread('lena.jpg',1)
print(img)
cv.imshow('image',img)
k=cv.waitKey()
if k==27:
    cv.destroyAllWindows()
elif k== ord('s'):
    cv.imwrite('lena_copy.png',img)'''
''''''''''''''''''''''''''''''

'''cap=cv.VideoCapture(0);
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('output.avi',fourcc,20.0,(640,480))

print(cap.isOpened())
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('frame',gray)
        if cv.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()'''
''''''''''''''''''''''''''''''''''''''''''


'''img= cv.imread('lena.jpg',1)
#img=np.zeros([512,512,0],)

img=cv.line(img,(0,0),(255,255),(0,0,255),5)
img=cv.rectangle(img,(0,0),(280,240),(240,0,0),-1)
font=cv.FONT_HERSHEY_COMPLEX
img=cv.putText(img,'Hitanshu',(40,40),font,0.80,(0,255,0),2)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()'''
''''''''''''''''''''''''''''''

'''cap=cv.VideoCapture(0);
print(cap.get(3))
print(cap.get(4))
cap.set(3,440)
cap.set(4,280)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        #out.write(frame)
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('frame',gray)
        if cv.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break
cap.release()
#out.release()
cv.destroyAllWindows()'''
###################################

'''cap=cv.VideoCapture(0);
print(cap.get(3))
print(cap.get(4))
cap.set(3,440)
cap.set(4,280)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        #out.write(frame)
        font=cv.FONT_HERSHEY_DUPLEX
        date=str(datetime.datetime.now())
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        new=cv.putText(frame,date,(10,50),font,1.0,(127,10,250),4)
        cv.imshow('frame',new)
        if cv.waitKey(1) & 0xFF== ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()'''
###################################


'''#events= [i for i in dir(cv) if 'EVENT' in i]
#print (events)
def click_event(event,x,y,flag,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font=cv.FONT_HERSHEY_DUPLEX
        strxy= str(x)+','+str(y)
        cv.putText(img,strxy,(x,y),font,0.5,(44,22,196),2)
        cv.imshow('image',img)

    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv.FONT_HERSHEY_DUPLEX
        strxy= str(blue)+','+str(green)+','+str(red)
        cv.putText(img,strxy,(x,y),font,0.5,(250,250,250),2)
        cv.imshow('image',img)
img=cv.imread('lena.jpg',1)
cv.imshow('image',img)

cv.setMouseCallback('image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()'''

###############################

''''def click_event(event,x,y,flag,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),3,(0,0,230),-1)
        points.append((x,y))
        if len(points)>=2:
            cv.line(img,points[-1],points[-2],(0,0,230),3)
        cv.imshow('image',img)
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv.circle(img,(x,y),3,(0,0,255),-1)
        myimage=cv.imread('lena.jpg',1)
        myimage[:]=[blue,green,red]
        cv.imshow('particular_color',myimage)
    
img=cv.imread('lena.jpg',1)
cv.imshow('image',img)
points=[]
cv.setMouseCallback('image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()'''

##############################################################

'''img= cv.imread('messi5.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
#b,g,r=cv.split(img)
#img=cv.merge((b,g,r)) 

# Select ROI 
r = cv.selectROI("select the area", img) 

# Crop image 
cropped_image = img[int(r[1]):int(r[1]+r[3]), 
					int(r[0]):int(r[0]+r[2])] 
img=cv.resize(img,(512,512))
cropped_image=cv.resize(cropped_image,(512,512))
dst=cv.addWeighted(img,0.5,cropped_image,0.5,0)

# Display cropped image 
cv.imshow("Final", dst) 
cv.waitKey(0) 


cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()
'''
#############################################
'''def nothing(x):
    print(x)
cv.namedWindow('My-Image')
cv.createTrackbar('cp','My-Image',10,400,nothing)
switch='color/gray'
cv.createTrackbar(switch,'My-Image',0,1,nothing)
while(1):
    img=cv.imread('lena.jpg',1)
    pos=cv.getTrackbarPos('cp','My-Image')
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(50,150),font,4,(0,0,255),3)
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    s=cv.getTrackbarPos(switch,'My-Image')
    if s==0:
        pass
    else:
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    img=cv.imshow('My-Image',img)

cv.destroyAllWindows()'''

###########################################
 
'''def nothing(x):
    pass
cap=cv.VideoCapture(0)
cv.namedWindow("Tracking")
cv.createTrackbar("Lh","Tracking",0,255,nothing)
cv.createTrackbar("LS","Tracking",0,255,nothing)
cv.createTrackbar("LV","Tracking",0,255,nothing)
cv.createTrackbar("UH","Tracking",255,255,nothing)
cv.createTrackbar("US","Tracking",255,255,nothing)
cv.createTrackbar("UV","Tracking",255,255,nothing)



while(True):
    ret,frame=cap.read()
    hsv= cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_h=cv.getTrackbarPos("Lh","Tracking")
    l_s=cv.getTrackbarPos("LS","Tracking")
    l_v=cv.getTrackbarPos("LV","Tracking")
    u_h=cv.getTrackbarPos("UH","Tracking")
    u_s=cv.getTrackbarPos("US","Tracking")
    u_v=cv.getTrackbarPos("UV","Tracking")
    
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,l_b,u_b)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("Frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    key=cv.waitKey(1)
    if key==27:
        break
cap.release()
cv.destroyAllWindows()'''

######################################################

'''Thresholding and Adaptive Thresholding'''

''''img=cv.imread('gradient.png',1)
ret,th1=cv.threshold(img,50,255,cv.THRESH_BINARY)
ret,th2=cv.threshold(img,200,255,cv.THRESH_BINARY_INV)
ret,th3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles=['Original Image','Binary','Binary Inverse','Trunc','Torezo','Torezo inverse']
images=[img,th1,th2,th3,th4,th5]
 
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()'''

#######################################################

'''img=cv.imread('smarties.png',0)
ret,mask=cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernel=np.ones((3,3),np.uint8)
dilation=cv.dilate(mask,kernel=kernel,iterations=2)
erosion=cv.erode(mask,kernel=kernel,iterations=2)
opening= cv.morphologyEx(mask,cv.MORPH_OPEN, kernel)

titles=['Original Image','mask','dilation','erosion','opening']
images=[img,mask,dilation,erosion, opening]
 
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()'''

########################################

'''morphological operation'''

#########################################

'''img= cv.imread('smarties.png')
img_gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh=cv.threshold(img_gray,200,255,0)
contours, hierachy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print("Number of contours:"+str(len(contours)))
cv.drawContours(img,contours,-1,(0,0,0),3)
cv.imshow('Contour Detection',img)
cv.waitKey(0)
cv.destroyAllWindows()'''

######################################################################

cap=cv.VideoCapture(0)
ret,frame1= cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    diff=cv.absdiff(frame1,frame2)
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    __,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dilated=cv.dilate(thresh,None,iterations=5)
    contours, hierachy=cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        (x,y,w,h)=cv.boundingRect(contour)
        area=cv.contourArea(contour)
        if area <8000:
            continue
        elif area>8000 and area<50000:

            cv.rectangle(frame1,(x,y),(x+w ,y+h),(0,255,0),2)
            cv.putText(frame1,"Status: {}".format('Movement'),(10,20),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
        elif area>100000:
            cv.putText(frame1,"Status: {}".format('Tampering is being done'),(10,20),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    cv.imshow('feed',frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv.waitKey(40) == 27:
        break


cap.release()
cap.destroyAllWindows()


