#t.ly/CzNT
import cv2
import time
import pyttsx3 #離線語音 gtts<-Google需要上網
import numpy
from PIL import ImageFont, ImageDraw, Image
duration = 500  # millisecond
freq = 1040  # Hz
# 引入人像識別訓練庫 haarcascade_frontalface_default.xml
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_patterns = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_patterns = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
font = ImageFont.truetype('msjhbd.ttc', 40)
fillColor = (255,0,0)
# 讀取圖片201807_OpenCVFace\haarcascade_eye.xml
#sample_image = cv2.imread('3.jpg')
#gray = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)
# 獲取識別到的人臉                      (偵測的圖,每次放大多少去偵測,閥值預設3,從多少開始偵測
#faces = face_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(150, 150),maxSize=(500,500))
#eyes= eyes_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(10, 10),maxSize=(500,500))
# 將識別到的人臉框出來
cap = cv2.VideoCapture(0)
count=0
maskflag=0
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(150, 150),maxSize=(500,500))    
    for (x, y, w, h) in faces:                          #顏色       寬度
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 10)
        pic_gray=gray[y:y+h, x:x+w]
        cv2.imshow("face", pic_gray)
        eyes= eyes_patterns.detectMultiScale(pic_gray,scaleFactor=1.15,minNeighbors=5,minSize=(10, 10),maxSize=(500,500))
        #for (x1, y1, w1, h1) in eyes:                          #顏色       寬度
            #cv2.rectangle(frame, (x1+x, y1+y), (x+x1+w1, y+y1+h1), (0, 0, 255), 20)            
        pic_gray2=gray[y+int(h/2):y+h, x:x+w] #擷取下半張臉
        cv2.imshow("face2", pic_gray2)
        mouth= mouth_patterns.detectMultiScale(pic_gray2,scaleFactor=1.5,minNeighbors=5,minSize=(10, 10),maxSize=(500,500))
        print(len(mouth))
        if (len(mouth)>0):                        
            for (x2, y2, w2, h2) in mouth:                          #顏色       寬度
                #cv2.rectangle(pic_gray2, (x2, y2), (x2+w2,y2+h2), (255, 255, 255), 10)
                cv2.imshow("face2", pic_gray2)
            count=count+1
            if (count>5):    #連續五次看到嘴巴
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0, 255), 20)
                img_PIL = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(img_PIL)
                draw.text((x,y-50), '請戴上口罩', font=font, fill=fillColor)
                frame = cv2.cvtColor(numpy.asarray(img_PIL),cv2.COLOR_RGB2BGR)
                #count=0
                maskflag=1
                #顯示文字
                print("請戴上口罩")                    
        else:
            count=0    
    cv2.imshow("output", frame)
    c = cv2.waitKey(10)
    if (maskflag==1):
        #發出聲音        
        time.sleep(1)#delay
        maskflag=0
        engine = pyttsx3.init()
        engine.say("請戴上口罩")
        engine.runAndWait()
        time.sleep(3)
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break

