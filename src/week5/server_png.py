import cv2
import socket
import time
import struct
import numpy as np

host = "192.168.56.101"
port = 5000
path = "./tilesu_king.png"
img = cv2.imread(path)
img = cv2.resize(img,(640,480))
cv2.imwrite("./resize.jpg",img)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
fin_message = "__end__"

sock = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
sock.bind((host,port))

while True:
  try:
    print("waiting...")
    message,client_addr = sock.recvfrom(1024)
    message = message.decode(encoding="utf-8")
    print("receive request message:{}".format(message))
    time.sleep(1)
    print("serve img")
    result,img_data = cv2.imencode(".jpg",img,encode_param)
    for pack in np.array_split(img_data,10):
      sock.sendto(pack.tostring(),client_addr)
    sock.sendto(fin_message.encode("utf-8"),client_addr)
    print("fin push img")
  except KeyboardInterrupt:
    print("fin server")
    sock.close()
    break
