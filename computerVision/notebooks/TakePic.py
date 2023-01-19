#t.ly/GhMA
import cv2

# 選擇第1隻攝影機
cap = cv2.VideoCapture(0)
picId=0
while cap.isOpened():#鏡頭能開啟嗎？
  # 從攝影機擷取一張影像
  ret, frame = cap.read() #ret=retval(True:正常、False:不正常),frame=image    
  # 顯示圖片
  cv2.imshow('frame', frame)
  #轉成灰階
  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #cv2.imshow('gray', gray)
  #轉成90度
  #tranframe = cv2.transpose(frame)  
  #cv2.imshow('tran', tranframe)
  #frame=cv2.flip(frame,0) #1:左右鏡像，0:上下左右顛倒，-1:上下顛倒
  #cv2.imshow('flip', frame)
  # 按a拍照存檔
  key=cv2.waitKey(1)#0=強制等待、1:等候1ms就跳過  更新影像
  if key == ord('a'): #使用者按了鍵盤'a'
    cv2.imwrite(str(picId)+".jpg", frame)
    picId=picId+1
  # 按q離開
  if key == ord('q'): #使用者按了鍵盤'q'
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
