#t.ly/oq-S
import cv2
# 引入人像識別訓練庫 haarcascade_frontalface_default.xml
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_patterns = cv2.CascadeClassifier('haarcascade_eye.xml')
# 讀取圖片
sample_image = cv2.imread('0.jpg')
gray = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)
# 獲取識別到的人臉                      (偵測的圖,每次放大多少去偵測,閥值預設3,從多少開始偵測50*1.15=57.5
faces = face_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=3,minSize=(50, 50),maxSize=(500,500))
#eyes= eyes_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(10, 10),maxSize=(500,500))
# 將識別到的人臉框出來
for (x, y, w, h) in faces:                          #顏色       寬度
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 5)
        
    eyes= eyes_patterns.detectMultiScale(sample_image[y:y+h,x:x+w],scaleFactor=1.1,minNeighbors=2,minSize=(5, 5),maxSize=(500,500))
    for (x1, y1, w1, h1) in eyes:                          #顏色       寬度
        cv2.rectangle(sample_image, (x1+x, y1+y), (x+x1+w1, y+y1+h1), (0, 0, 255), 5)
# 生成一張新的圖片儲存識別結果
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imwrite('output.jpg', sample_image)
cv2.imshow("output", sample_image)
cv2.waitKey(0)



