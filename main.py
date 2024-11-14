from PIL import ImageGrab, Image
import cv2
import time
import mouse
time.sleep(2)
# mouse.press()
# time.sleep(2)
# mouse.release()


y = 445
x = 1096
h = 221
w = 13

box = (1096,445,1109,666)

ss = ImageGrab.grab()
ss2 = ss.crop(box)

img = cv2.imread(r"C:\Users\LUCAS\Desktop\code\python\auto fisch\dsdsq.png")
cropped = img[x:w, y:h]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)


ss2.show()
ss2.save("zz.png")