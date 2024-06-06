import cv2
import matplotlib.pyplot as plt
import os
import uuid


posit_path=os.path.join('data','positive')
anchor_path=os.path.join('data','anchor')

#os.makedirs(posit_path)
#os.makedirs(anchor_path)






#os.path.join()
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    frame=frame[120:300+120,200:550,:]
    if not ret:
        break

    # Display the frame in a window
    cv2.imshow("image", frame)

    # Exit the loop when 'q' is pressed

   # if cv2.waitKey(1) &0xFF==ord('a'):
    
    #imgname=os.path.join(anchor_path,'{}.jpg'.format(uuid.uuid1()))
     #   cv2.imwrite(imgname,frame)

    if cv2.waitKey(1) & 0xFF==ord('p'):
        imgname=os.path.join(posit_path,'{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Show the last captured frame using matplotlib
plt.imshow(frame)
plt.title("Last Captured Frame")
plt.show()

print(frame.shape)

cap.release()
cv2.destroyAllWindows()
