import cv2
import dlib

#選擇攝影機
cap = cv2.VideoCapture(0)
#取得預設的臉部偵測器
detector = dlib.get_frontal_face_detector()
#根據shape_predictor方法載入68個特徵點模型，此方法為人臉表情識別的偵測器
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
  #當攝影機打開時，對每個frame進行偵測
while(cap.isOpened()):
    #讀出frame資訊
    ret, frame = cap.read()
    #如果CSI鏡頭就不要resize
    frame=cv2.resize(frame,(640,480))
    #偵測人臉
    face_rects, scores, idx = detector.run(frame, 0)
    #取出偵測的結果
    for i, d in enumerate(face_rects):
      x1 = d.left()
      y1 = d.top()
      x2 = d.right()
      y2 = d.bottom()
      text = " %2.2f ( %d )" % (scores[i], idx[i])

      #繪製出偵測人臉的矩形範圍
      cv2.rectangle(frame, (x1, y1), (x2, y2), ( 0, 255, 0), 4, cv2. LINE_AA)

      #標上人臉偵測分數與人臉方向子偵測器編號
      cv2.putText(frame, text, (x1, y1), cv2. FONT_HERSHEY_DUPLEX,
      0.7, ( 255, 255, 255), 1, cv2. LINE_AA)
 
      #給68特徵點辨識取得一個轉換顏色的frame
      landmarks_frame = cv2.cvtColor(frame, cv2. COLOR_BGR2RGB)

      #找出特徵點位置
      shape = predictor(landmarks_frame, d)    
      x38=0
      y38=0
      x41=0
      y41=0
      #繪製68個特徵點
      for i in range( 68):
        cv2.circle(frame,(shape.part(i).x,shape.part(i).y), 3,( 0, 0, 255), 2)
        cv2.putText(frame, str(i),(shape.part(i).x,shape.part(i).y),cv2. FONT_HERSHEY_COMPLEX, 0.5,( 255, 0, 0), 1)
        if i==38:
            print("x38=",shape.part(i).x,shape.part(i).y)
            x38=shape.part(i).x
            y38=shape.part(i).y
        if i==41:
            print("x41=",shape.part(i).x,shape.part(i).y)
            x41=shape.part(i).x
            y41=shape.part(i).y
      print("y41-y38=",y41-y38)
    #輸出到畫面
   
    cv2.imshow( "Face Detection", frame)

    #如果按下q键，就退出
    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
       break
#釋放記憶體
cap.release()
#關閉所有視窗
cv2.destroyAllWindows()




