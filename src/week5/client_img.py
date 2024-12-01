import socket
import cv2
import struct
import numpy as np

host = "192.168.56.101"
port = 5000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
    message = input()
    print("request message:{}".format(message))
    send_len = sock.sendto(message.encode("utf-8"),(host,port))
    print("waiting response from server")
    pack_img = bytes()
    while True:
        data,addr = sock.recvfrom(1024*64)
        if len(data) == 7 and data == b"__end__":break
        pack_img += data

    nannay = np.frombuffer(pack_img,dtype=np.uint8)
    img = cv2.imdecode(nannay,1)
    cv2.imwrite("./downloda_img.jpg",img)
    cv2.imshow("img",img)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

except KeyboardInterrupt:
        cv2.destroyAllWindows()
        sock.close()
