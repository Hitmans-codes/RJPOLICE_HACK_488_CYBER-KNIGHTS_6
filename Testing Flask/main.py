from flask import Flask ,render_template
import cv2 as cv
import numpy as np
import datetime
from matplotlib import pyplot as plt
app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/index.html')
def backtoHome():
    return render_template('index.html')
def hello_world():
    return render_template('index.html')
@app.route('/index3.html',methods=['POST','GET'])
def newpage_redirectioin():
    return render_template('index3.html')
@app.route('/index2.html',methods=['POST','GET'])
def console_page():
    return render_template('index2.html')
@app.route('/table.html',methods=['POST','GET'])
def table_page():
    return render_template('table.html')
@app.route('/maps.html',methods=['POST','GET'])
def map_page():
    return render_template('maps.html')
@app.route('/notifications.html',methods=['POST','GET'])
def notifications_page():
            str=''
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
                        str='Tampering is being done'
                        cv.putText(frame1,"Status: {}".format('Tampering is being done'),(10,20),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
                cv.imshow('feed',frame1)
                frame1=frame2
                ret,frame2=cap.read()

                if cv.waitKey(40) == 27:
                    break


            
            cap.release()
            
            return render_template('notifications.html',something=str) 

if __name__=="__main__":
  app.run( debug=True,port=8000)