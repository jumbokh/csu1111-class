#t.ly/vwPO
import cv2
# 引入人像識別訓練庫 haarcascade_frontalface_default.xml
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_patterns = cv2.CascadeClassifier('haarcascade_eye.xml')

# 選擇第1隻攝影機
cap = cv2.VideoCapture(0)
picId=0
while cap.isOpened():#鏡頭能開啟嗎？
    ret, frame = cap.read() #ret=retval(True:正常、False:不正常),frame=image    
    # 顯示圖片
    frame=cv2.flip(frame,1) #1:左右鏡像，0:上下左右顛倒，-1:上下顛倒
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 獲取識別到的人臉                      (偵測的圖,每次放大多少去偵測,閥值預設3,從多少開始偵測50*1.15=57.5
    faces = face_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=3,minSize=(50, 50),maxSize=(500,500))
    #eyes= eyes_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(10, 10),maxSize=(500,500))
    # 將識別到的人臉框出來
    for (x, y, w, h) in faces:                          #顏色  bgr  寬度
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
           
        eyes= eyes_patterns.detectMultiScale(gray[y:y+h,x:x+w],scaleFactor=1.1,minNeighbors=2,minSize=(5, 5),maxSize=(500,500))
        for (x1, y1, w1, h1) in eyes:                                     #顏色       寬度
            cv2.rectangle(frame, (x1+x, y1+y), (x+x1+w1, y+y1+h1), (0, 0, 255), 5)
    cv2.imshow("output", frame)
    key=cv2.waitKey(1)#0=強制等待、1:等候1ms就跳過  更新影像
    if key == ord('a'): #使用者按了鍵盤'a'
        cv2.imwrite(str(picId)+".jpg", frame)
        picId=picId+1
    # 按q離開
    if key == ord('q'): #使用者按了鍵盤'q'
        break #強制退出while迴圈

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()


