import cv2
cap=cv2.VideoCapture(0)
i=0
while(True):
  ret,frame=cap.read()
  cv2.imshow("Live Video",frame)
  if (cv2.waitKey(1) & 0xFF == ord('c')):
    print('c')
    cv2.imwrite("C:\\Users\R I B\Desktop\wooow\images\capture\capture"+str(i)+".jpg",frame)
    i=i+1
  if(cv2.waitKey(1) & 0xFF == ord('q')):
    cap.release()
    cv2.destroyAllWindows()